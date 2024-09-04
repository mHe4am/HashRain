#!/usr/bin/env python3
import sys
from hash_rain.HashRain_Gen import main as generator
from hash_rain.HashRain_Cracker import main as cracker


def show_usage():
    print("\nUsage:")
    print(f"[+] python3 {sys.argv[0]} generate <Algorithm> <Wordlist>")
    print(f"[+] python3 {sys.argv[0]} crack <Hash>\n")
    print(f"Examples:")
    print(f"[+] python3 {sys.argv[0]} generate sha1 ./rockyou.txt")
    print(f"[+] python3 {sys.argv[0]
                         } crack e6b6afbd6d76bb5d2041542d7d2e3fac5bb05593\n")


def main():
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == "generate":
        generator()
    elif command == "crack":
        cracker()
    else:
        print(f"[-] Unknown Command: {command}")
        print(f"[*] Use 'generate' or 'crack'.\n")
        show_usage()


if __name__ == '__main__':
    main()
