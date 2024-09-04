#!/usr/bin/env python3
"""
Hashing a list of Strings and storing a Hash-String pairs.
"""

# Import required modules
import os
import sys
import pickle
import hashlib


# Store Data (Serialization)
def storeData(data: dict, saveFile):
    try:
        with open(saveFile, 'wb') as file:
            pickle.dump(data, file)
    except PermissionError:
        print("\n[-] Permission denied: Unable to write to the file.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] An unexpected error occurred (while storing data): {e}")
        sys.exit(1)


# Load Data (Deserialization)
def loadData(loadFile):
    """
    Loads Serialized data from a file.
    """
    try:
        if not os.path.exists(loadFile):
            return {}
        if os.path.getsize(loadFile) > 0:
            with open(loadFile, 'rb') as file:
                data = pickle.load(file)
                return data
        else:
            return {}
    except PermissionError:
        print("\n[-] Permission denied: Unable to read the file.")
        sys.exit(1)
    except FileNotFoundError:
        return {}
    except pickle.UnpicklingError:
        print("\n[-] Error importing the data.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] An unexpected error occurred (while loading data): {e}")
        sys.exit(1)


# Load wordlist from a file
def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            # strips and removes empty lines, returns a list/array
            wordlist = [line.strip() for line in file if line.strip()]
        return wordlist
    except PermissionError:
        print("\n[-] Permission denied: Unable to read the file.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n[-] File not found.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] An unexpected error occurred (while reading file): {e}")
        sys.exit(1)


# Hashing Function
def hashing(inputString, hashingAlgo):
    """
      Hashes the input string using the specified hashing algorithms.
    """

    if not inputString:
        return False

    availableHashes = ['md5', 'sha1', 'sha256', 'sha512']
    if hashingAlgo not in availableHashes:
        print("\n[-] Not available Hash Algorithm.")
        print("[*] Available Hash Algorithms: ['md5', 'sha1', 'sha256', 'sha512']\n")
        sys.exit(0)

    # Hash the pass
    inputString = inputString.encode()  # Encode to bytes for hashing
    if hashingAlgo == 'md5':
        hashed = hashlib.md5(inputString)
    elif hashingAlgo == 'sha1':
        hashed = hashlib.sha1(inputString)
    elif hashingAlgo == 'sha256':
        hashed = hashlib.sha256(inputString)
    elif hashingAlgo == 'sha512':
        hashed = hashlib.sha512(inputString)

    # Convert to Hexadecimal
    finalHash = hashed.hexdigest()

    return finalHash


# Rainbow Table Generator
def rainbow_table_gen(wordlist, hashingAlgo):
    hashes = {}

    for string in wordlist:
        hashedPass = hashing(string, hashingAlgo)
        hashes[hashedPass] = string

    return hashes


# Run Main Functions
def main():
    if (len(sys.argv) < 4):
        print(f"\nUsage: \"python3 {
              sys.argv[0]} generate <Algorithm> <Wordlist>\"")
        print(f"Example: \"python3 {
              sys.argv[0]} generate sha1 ./rockyou.txt\"\n")
        sys.exit(0)

    hashingAlgo = sys.argv[2]
    wordlist = sys.argv[3]
    inputStrings = readFile(wordlist)
    dataFilePath = f"./data/{hashingAlgo}-rainbow_table.pkl"

    new_rainbow_table = rainbow_table_gen(inputStrings, hashingAlgo)

    existing_rainbow_table = loadData(dataFilePath)  # Load current data
    existing_rainbow_table.update(new_rainbow_table)  # Merge both tables
    storeData(existing_rainbow_table, dataFilePath)  # Store data

    # print("[+] 0/10,000 Input Hashed")
    print("\n[+] Finished.")
    print(f"[+] Saved Path: \"{os.path.abspath(dataFilePath)}\".\n")


# Run the Script
if __name__ == '__main__':
    main()
