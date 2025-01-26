#!/usr/bin/env python3
"""
fix_checksum.py

Usage:
    python3 fix_checksum.py <input.bin> <output.bin>

1) Ensures that the byte at offset 0x02 in the ROM is set to the number of
   512-byte blocks (ROM size).
2) Ensures that the 8-bit sum of the entire ROM is zero modulo 256.

Example:
    If your final ROM is 1024 bytes (2 blocks of 512), this script writes 0x02
    to offset 2, then fixes the last byte so the entire file sums to 0 (mod 256).
"""

import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: fix_checksum.py <input.bin> <output.bin>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Read the entire ROM into memory
    with open(input_path, "rb") as f:
        rom_data = bytearray(f.read())

    # Calculate size in 512-byte blocks
    size_bytes = len(rom_data)
    if size_bytes % 512 != 0:
        print(f"Error: {input_path} size ({size_bytes} bytes) is not a multiple of 512!")
        sys.exit(1)

    size_blocks = size_bytes // 512
    if size_blocks > 255:
        print(f"Error: ROM size in blocks ({size_blocks}) exceeds 255!")
        sys.exit(1)

    # 1) Patch the size byte at offset 2
    rom_data[2] = size_blocks

    # 2) Compute the checksum so the entire file sums to 0 (mod 256).
    #    The last byte is typically the checksum placeholder.
    sum_of_bytes = sum(rom_data[:-1]) & 0xFF
    rom_data[-1] = (-sum_of_bytes) & 0xFF

    # Write out the modified ROM
    with open(output_path, "wb") as f:
        f.write(rom_data)

    print(f"[+] Patched size byte to {size_blocks} at offset 2.")
    print(f"[+] Fixed checksum => {output_path} (sum of bytes = 0 mod 256)")

if __name__ == "__main__":
    main()
