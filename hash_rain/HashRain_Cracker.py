#!/usr/bin/env python3
"""
Searches a list of precomputed hashed strings to find the matched hash.
"""

# Import required modules
import os
import sys
from hash_rain.HashRain_Gen import loadData


# Find if the hash exists in the Database
def searching(inputHash):
    print(f"[*] Searching for hash: {inputHash}\n")

    hashes_paths = {
        "md5": r".\data\md5-rainbow_table.pkl",
        "sha1": r".\data\sha1-rainbow_table.pkl",
        "sha256": r".\data\sha256-rainbow_table.pkl",
        "sha512": r".\data\sha512-rainbow_table.pkl"
    }

    for hashName, hashPath in hashes_paths.items():
        absolutePath = os.path.abspath(hashPath)
        print(f"[*] Loading data from: \"{absolutePath}\"")

        try:
            hashes_db = loadData(absolutePath)
            print(f"[+] {len(hashes_db)} Hash loaded from: \"{absolutePath}\"\n")
            if inputHash in hashes_db:
                return hashName, hashes_db[inputHash]
        except Exception as e:
            print(
                f"[-] Error while loading or searching in {hashName} database: {e}")

    print("[-] Hash not found in any database.")


# Run Main Functions
def main():
    if (len(sys.argv) < 3):
        print(f"\nUsage: \"python3 {sys.argv[0]} crack <Hash>\"")
        print(f"Example: \"python3 {
              sys.argv[0]} crack e6b6afbd6d76bb5d2041542d7d2e3fac5bb05593\"\n")
        sys.exit(0)

    inputHash = sys.argv[2].strip()
    searchResults = searching(inputHash)
    if (searchResults and len(searchResults) == 2):
        hashAlgorithm = searchResults[0]
        matchedHash = searchResults[1]

        if matchedHash:
            print("\n[+] Hash found!")
            print(f"[+] Algorithm: {hashAlgorithm}")
            print(f"[+] {inputHash}:{matchedHash}")
            print("\nEnjoy!\n")
        else:
            print("\n[-] Sorry, we couldn't crack your Hash!\n")


# Run the Script
if __name__ == '__main__':
    main()
