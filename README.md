# LegacyOptionRom

A minimal x86 **Legacy Option ROM** that prints "Hello World!", waits ~30 seconds, 
and returns control to the system BIOS. Demonstrates how to create and checksum a 
512-byte Option ROM recognized by legacy BIOS systems or emulators (e.g. Bochs, QEMU).

## Features

- Proper 0x55AA signature
- Waits ~30 seconds using BIOS timer ticks (~18.2Hz × 30s = ~546 ticks)
- Proper checksum so the BIOS accepts and runs the ROM

## Requirements

- **Ubuntu or similar Linux environment**  
- NASM (for assembling)  
- Python 3 (for fixing the checksum)  
- Bochs or QEMU to emulate the ROM

## Building & Running

1. **Clone & Enter Directory**  
   ```bash
   git clone https://github.com/DanielLundDev/LegacyOptionRom.git
   cd LegacyOptionRom
   ./build.sh
