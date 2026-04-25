from .protocol_mapper import map_protocol

class PacketParser:

    def parse(self, raw_packet: dict) -> dict:
        return {
            "timestamp": raw_packet["timestamp"],
            "src_ip": raw_packet["src_ip"],
            "dst_ip": raw_packet["dst_ip"],
            "src_port": raw_packet["src_port"],
            "dst_port": raw_packet["dst_port"],
            "protocol": map_protocol(raw_packet["protocol"]),
            "packet_size": raw_packet["packet_size"]
        }