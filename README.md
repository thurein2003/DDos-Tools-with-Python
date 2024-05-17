# DDoS Tools with Python

This repository contains tools for performing DDoS (Distributed Denial of Service) attacks using Python. These tools are intended for educational purposes only and should be used responsibly and legally.

## Disclaimer

**Warning:** Unauthorized DDoS attacks are illegal and unethical. This tool is provided for educational purposes only. The user is solely responsible for any misuse of this tool. Always obtain explicit permission before conducting any kind of network testing.

## Features

- Generate random IP addresses for spoofing
- Send TCP SYN packets
- Customizable packet size
- Verbose output option
- Logging option

## Requirements

- Python 3.x
- `scapy` library
- `tqdm` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/thurein2003/DDos-Tools-with-Python.git
    cd DDos-Tools-with-Python
    ```

2. Install the required libraries:
    ```sh
    pip install scapy tqdm
    ```

## Usage

Run the script with the following command:

```sh
python3 DDoSEchtit.py -t <target_ip> -p <target_port> -np <num_packets> -ps <packet_size> -v -l <log_file>


-t, --target: IP address of the target (required)
-p, --port: Port number of the target (required)
-np, --num-packets: Number of packets to send (default: 1000)
-ps, --packet-size: Packet size in bytes (default: 64)
-v, --verbose: Enable verbose output
-l, --log: Log file to record the attack details