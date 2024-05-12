from scapy.layers.inet import IP, TCP
from scapy.all import *

# Function to analyze and print packet information
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {proto}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Source Port: {src_port} | Destination Port: {dst_port}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("Payload:", payload)

# Main function
def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0, count=100)  # Stop after sniffing 100 packets

if __name__ == "__main__":
    main()
