import argparse
from .core import is_attack

def main():
    parser = argparse.ArgumentParser(description="Analyze pcap file for attacks.")
    parser.add_argument("pcap", help="Path to the .pcap file")
    args = parser.parse_args()

    if is_attack(args.pcap):
        print("🔴 Attack detected in the file!")
    else:
        print("🟢 No attack detected.")
