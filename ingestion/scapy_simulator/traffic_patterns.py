"""
Defines traffic behavior patterns
"""

import random

def normal_pattern(packet):
    packet["label"] = "normal"
    return packet

def scan_pattern(packet):
    packet["dst_port"] = random.choice(range(20, 1024))
    packet["label"] = "port_scan"
    return packet

def ddos_pattern(packet):
    packet["packet_size"] = random.randint(40, 100)
    packet["label"] = "ddos"
    return packet

PATTERNS = [normal_pattern, scan_pattern, ddos_pattern]