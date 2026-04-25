"""
Classifies IPs as internal or external.
"""

def is_internal_ip(ip: str) -> bool:
    return ip.startswith("10.") or ip.startswith("192.168.")