#!/usr/bin/env python3
"""Check which TCP ports are open on a host. Use it only on systems you own."""
import socket
import sys


def is_open(host, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "web01"
    for port in [22, 80, 443, 3000, 3306]:
        state = "open" if is_open(host, port) else "closed"
        print(f"{host}:{port} {state}")
