import pathlib
import sys
import pytest

# Allow tests to import the tools package from repository root
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from tools.ioc_scraper.regex_patterns import extract_iocs


def test_extract_iocs_detects_ioc_types():
    text = (
        "The attacker used IP 192.168.0.1 to connect to https://example.com/login. "
        "Contact user@example.com with the domain example.com for more info. "
        "sha256: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
        "md5: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    )
    results = extract_iocs(text)

    assert "192.168.0.1" in results["ipv4"]
    assert "https://example.com/login" in results["url"]
    assert "user@example.com" in results["email"]
    assert "example.com" in results["domain"]
    assert "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" in results["sha256"]
    assert "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" in results["md5"]

def test_extract_iocs_all_types_present():
    text = (
        "IP 10.0.0.1 and url http://example.org page. "
        "Email contact at admin@example.org. "
        "SHA256 ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff "
        "MD5 11111111111111111111111111111111"
    )
    results = extract_iocs(text)

    for key in ["ipv4", "url", "email", "domain", "sha256", "md5"]:
        assert results[key], f"{key} should not be empty"
