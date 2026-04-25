def parse_packet(packet):
    return {
        "timestamp": packet.get("timestamp"),
        "src_ip": packet.get("src_ip"),
        "dst_ip": packet.get("dst_ip"),
        "packet_size": packet.get("packet_size")
    }