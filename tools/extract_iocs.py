"""
Simple IOC extractor using regex. Replace with more robust parser for production.
"""
import re

# Simple IPv4 regex (not fully strict; for demo purposes)
IP_RE = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
URL_RE = re.compile(r"https?://[\w\-\.\:/\?=&%#]+")

def extract_iocs(text: str) -> dict:
    ips = IP_RE.findall(text)
    urls = URL_RE.findall(text)
    # deduplicate
    ips = list(dict.fromkeys(ips))
    urls = list(dict.fromkeys(urls))
    return {'ips': ips, 'urls': urls}