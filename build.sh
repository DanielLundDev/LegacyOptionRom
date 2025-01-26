#!/usr/bin/env bash
set -e

# Build script for the "Hello World Option ROM" project.
echo "[*] Assembling LegacyOptionRom.asm..."
nasm -f bin LegacyOptionRom.asm -o LegacyOptionRom.bin

echo "[*] Fixing checksum..."
python3 scripts/fix_checksum.py LegacyOptionRom.bin LegacyOptionRom_fixed.bin

echo "[*] Done."
echo " - LegacyOptionRom.bin        (raw binary, no checksum fix)"
echo " - LegacyOptionRom_fixed.bin  (final ROM with valid checksum)"
