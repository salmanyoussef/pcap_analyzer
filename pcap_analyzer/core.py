from scapy.all import rdpcap

def is_attack(pcap_path):
    packets = rdpcap(pcap_path)
    suspicious_count = 0

    for pkt in packets:
        if pkt.haslayer("TCP"):
            sport = pkt["TCP"].sport
            dport = pkt["TCP"].dport
            if dport == 4444 or sport == 4444:  # Common reverse shell port
                suspicious_count += 1

    return suspicious_count > 5  # Threshold
