# HashRain

## Overview

**HashRain** is a simple command-line tool designed to generate rainbow tables for some hashing algorithms and search for plaintext values corresponding to given hashes. The project is built using Python and allows users to crack hashed passwords efficiently using precomputed tables.


## Features

- Supports multiple hashing algorithms: `MD5`, `SHA1`, `SHA256`, `SHA512`.
- Generates rainbow tables from a wordlist.
- Searches for plaintext values in precomputed rainbow tables.
- Handles potential errors during file operations gracefully.


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mHe4am/HashRain.git
   cd HashRain
   ```

2. **Ensure Dependencies:**
   - Python 3.x
   - No external libraries required (uses Python's built-in modules)


## Usage

### 1. Generating Rainbow Tables

To generate a rainbow table for a specific hashing algorithm:

```bash
python3 hash_rain/HashRain_Gen.py <Algorithm> <Wordlist>
```

Example:
```bash
python3 hash_rain/HashRain_Gen.py sha1 ./rockyou.txt
```

This will create a `.pkl` file containing the hash-to-plaintext mappings in the `data` directory.

### 2. Cracking a Hash

To search for a plaintext value corresponding to a given hash:

```bash
python3 hash_rain/HashRain_Cracker.py <Hash>
```

Example:
```bash
python3 hash_rain/HashRain_Cracker.py e6b6afbd6d76bb5d2041542d7d2e3fac5bb05593
```

If the hash is found in the rainbow table, the corresponding plaintext value will be displayed.


## To Do
- [x] Implement additional hashing algorithms beyond MD5
- [x] Allow dynamic selection of hashing algorithms
- [x] Verify functionality with various passwords and hashing algorithms
- [ ] Add support for more hashing algorithms
- [ ] Provide an option to search within specific databases (e.g., SHA-1 only) (Cracker)
- [ ] Exclude databases based on hash length (Cracker)
- [ ] Implement functionality to crack a list of hashes (e.g., `hashes.txt`)


## Contributing

Any improvements or suggestions are welcome!
