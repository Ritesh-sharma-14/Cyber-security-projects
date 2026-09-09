import socket
from concurrent.futures import ThreadPoolExecutor


class PortScanner:

    def __init__(self, target, start_port, end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []

    def scan_port(self, port):

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((self.target, port))

            if result == 0:
                self.open_ports.append(port)

            sock.close()

        except Exception:
            pass


    def scan(self):

        print(f"\nScanning {self.target}...\n")

        with ThreadPoolExecutor(max_workers=100) as executor:

            for port in range(self.start_port, self.end_port + 1):
                executor.submit(self.scan_port, port)

        return sorted(self.open_ports)
