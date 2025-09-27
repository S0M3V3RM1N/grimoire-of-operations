# This tool is to only be used in a controlled environment on a network / device you own or have permission to test.
# Unauthorized use of this tool is prohibited. The author is not responsible for any damage caused by misuse of this tool.
# Use at your own risk.

# Python Packet Sniffer Tool for Linux (AF_PACKET)
# - Printer packet summaries (Ethernet, IP, TCP, UDP)
# - Heuristic for SYN-scan detection and high-rate DNS queries
# - Optional PCAP file writing
# Author: S0M3V3RM1N

# Usage: sudo python3 sniffer.py -i <interface> [-w <pcap_file_name>.pcap]

import socket
import struct
import time
import argparse
import collections
import os
import sys

# PCAP writer helpers 
PCAP_GLOBAL_HEADER_FMT = '<IHHIIII'
PCAP_PACKET_HEADER_FMT = '<IIII'

def pcap_global_header():
    return struct.pack(PCAP_GLOBAL_HEADER_FMT,
                       0xa1b2c3d4,  # Magic number
                       2,           # Major version number
                       4,           # Minor version number
                       0,           # GMT to local correction
                       0,           # Accuracy of timestamps
                       65535,       # Max length of captured packets, in octets
                       1)           # Data link type (Ethernet)

def pcap_packet_header(ts_sec, ts_usec, caplen, origlen):
    return struct.pack(PCAP_PACKET_HEADER_FMT, int(ts_sec), int(ts_usec), caplen, origlen)

# low-level header parsers
def mac_addr(raw):
    return ':'.join('{:02x}'.format(b) for b in raw)

def ipv4_addr(raw):
    return '.'.join(str(b) for b in raw)

def parse_ethernet_frame(data):
    if len(data) < 14:
        return None
    dst, src, proto = struct.unpack('!6s6sH', data[:14])
    return {
        'dest_mac': mac_addr(dst),
        'src_mac': mac_addr(src),
        'eth_proto': socket.htons(proto),
        'payload': data[14:],
    }

def parse_ipv4_packet(data):
    if len(data) < 20:
        return None
    ver_ihl = data[0]
    version = ver_ihl >> 4
    ihl = (ver_ihl & 0x0F) * 4
    total_length = struct.unpack('!H', data[2:4])[0]
    proto = data[9]
    src = ipv4_addr(data[12:16])
    dst = ipv4_addr(data[16:20])
    payload = data[ihl:total_length]
    return {
        'version': version,
        'ihl': ihl,
        'total_length': total_length,
        'protocol': proto,
        'src_ip': src,
        'dest_ip': dst,
        'payload': payload,
    }

def parse_tcp_segment(data):
    if len(data) < 20:
        return None
    src_port, dst_port, seq, ack, offset_reserved_flags = struct.unpack('!HHIIH', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flags = offset_reserved_flags & 0x01ff # lower 9 bits for flags
    payload = data[offset:]
    return {
        'src_port': src_port,
        'dest_port': dst_port,
        'seq': seq,
        'ack': ack,
        'offset': offset,
        'flags': flags,
        'payload': payload,
    }

def parse_udp_segment(data):
    if len(data) < 8:
        return None
    src_port, dst_port, length, checksum = struct.unpack('!HHHH', data[:8])
    payload = data[8:length]
    return {
        'src_port': src_port,
        'dest_port': dst_port,
        'length': length,
        'checksum': checksum,
        'payload': payload,
    }

# Simple heuristics trackers
class Heuristics:
    def __init__(self, syn_threshold=20, syn_window=10, dns_threshold=30, dns_window=10):
        # track SYN counts: {src_ip: deque of timestamps}
        self.syn_times = collections.defaultdict(collections.deque)
        self.syn_threshold = syn_threshold
        self.syn_window = syn_window

        # track DNS query counts: {src_ip: deque of timestamps}
        self.dns_times = collections.defaultdict(collections.deque)
        self.dns_threshold = dns_threshold
        self.dns_window = dns_window

        def note_syn(self, src):
            now = time.time()
            dq = self.syn_times[src]
            dq.append(now)
            # pop old entries
            while dq and now - dq[0] > self.syn_window:
                dq.popleft()
            if len(dq) > self.dns_threshold:
                return True, len(dq)
            return False, len(dq)
        
        # Main sniffer
        def run_sniffer(interface, pcap_out=None):
            if os.geteuid() != 0:
                print("ERROR: must run as root. Use sudo.")
                sys.exit(1)

            print(f"[+] Opening raw socket on interface: {interface}")
            try:
                raw_sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
                raw_sock.bind((interface, 0))
            except Exception as e:
                print("ERROR opening socket:", e)
                sys.exit(1)

            pcap_file = None
            if pcap_out:
                pcap_file = open(pcap_out, 'wb')
                pcap_file.write(pcap_global_header())
                print(f"[+] Writing packets to PCAP file: {pcap_out}")

            heur = Heuristics()

            try:
                while True:
                    packet, addr = raw_sock.recvfrom(65535)
                    ts = time.time()
                    eth = parse_ethernet_frame(packet)
                    if not eth: continue

                    # Basic display
                    eth_proto = eth['eth_proto']
                    if eth_proto == 8: # IPv4
                        ip = parse_ipv4_packet(eth['payload'])
                        if not ip: continue
                        proto = ip['proto']
                        src = ip['src']
                        dst = ip['dst']

                        human = f"{time.strftime('%H:%M:%S', time.localtime(ts))} {src} -> {dst} proto={proto}"
                        suspicious = []

                        if proto == 6: # TCP
                            tcp = parse_tcp_segment(ip['payload'])
                            if not tcp: continue
                            human += f" TCP {tcp['src_port']} -> {tcp['dest_port']} flags={tcp['flags']}"
                            # SYN flag: 0x02 (bit for SYN in lower bits usually 0x02)
                            SYN_FLAG = 0x02
                            if tcp['flags'] & SYN_FLAG:
                                syn_alert, count = heur.note_syn(src)
                                if syn_alert:
                                    suspicious.append(f"Possible SYN-scan from {src} ({count} SYNs in last {heur.syn_window}s)")
                        elif proto == 17: # UDP
                            udp = parse_udp_segment(ip['payload'])
                            if not udp: continue
                            human += f" UDP {udp['src_port']} -> {udp['dest_port']} len={udp['length']}"
                            # Basic DNS detection: DNS typically on port 53 and payload length > 12
                            if udp['dest_port'] == 53 or udp['src_port'] == 53:
                                dns_alert, count = heur.note_dns(src)
                                if dns_alert:
                                    suspicious.append(f"High-rate DNS queries from {src} ({count} queries in last {heur.dns_window}s)")

                        if suspicious:
                            print("!!! SUSPICIOUS:", human)
                            for s in suspicious: print("    >>", s)
                        else:
                            print(human)

                    # Optionally write raw packet to PCAP
                    if pcap_file:
                        ts_sec = int(ts)
                        ts_usec = int((ts - ts_sec) * 1_000_000)
                        caplen = len(packet)
                        pcap_file.write(pcap_packet_header(ts_sec, ts_usec, caplen, caplen))
                        pcap_file.write(packet)

            except KeyboardInterrupt:
                print("\n[+] Stopping sniffer (Ctrl-C).")
            finally:
                if pcap_file:
                    pcap_file.close()
                raw_sock.close()

        # CLI
        if __name__ == "__main__":
            parser = argparse.ArgumentParser(description="Simple Python Packet Sniffer (Linux).")
            parser.add_argument('-i', '--interface', required=True, help='Network interface to bind (e.g., eth0)')
            parser.add_argument('-w', '--write', dest='pcap', help='Write captured packets to PCAP file')
            args = parser.parse_args()
            run_sniffer(args.interface, args.pcap)