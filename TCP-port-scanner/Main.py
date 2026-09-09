from scanner import PortScanner
from banner import grab_banner


def main():

    print("""
=============================
      TCP PORT SCANNER
=============================
    """)

    target = input("Enter target IP/domain: ")

    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))


    scanner = PortScanner(
        target,
        start_port,
        end_port
    )


    open_ports = scanner.scan()


    if open_ports:

        print("\nOpen Ports Found:")

        for port in open_ports:

            banner = grab_banner(
                target,
                port
            )

            print(
                f"[+] Port {port} OPEN | {banner}"
            )

    else:

        print("\nNo open ports found.")



if __name__ == "__main__":
    main()
