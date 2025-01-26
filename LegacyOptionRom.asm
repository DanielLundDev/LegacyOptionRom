[org 0x0000]

ROM_Start:
    db 0x55, 0xAA           ; Option ROM signature
    db 0x01                 ; ROM size = 1 block (512 bytes)

start:
;-----------------------------------------------------------------------------
; Set DS = CS
; BIOS does not guarantee DS=CS, so we must manually synchronize them.
;-----------------------------------------------------------------------------
    push cs
    pop ds

    push cs
    pop ds

    ; 2) Force text mode 3
    mov ax, 0x0003
    int 0x10

    ; Print "Hello World!"
    mov si, msg_hello

.print_loop:
    lodsb
    or al, al
    jz .done_print
    mov ah, 0x0E
    int 0x10
    jmp .print_loop

.done_print:
    ; Delay ~30 seconds using ~18.2 Hz BIOS ticks (30 * 18.2 ~ 546)
    mov ah, 0x00
    int 0x1A          ; get current clock count in CX:DX
    mov bx, dx
    add bx, 546

.wait_loop:
    mov ah, 0x00
    int 0x1A
    cmp dx, bx
    jb .wait_loop

    ; Return to BIOS
    retf

; Our string data
msg_hello db "Hello World!", 0

; Pad/Checksum for 512 bytes
times (0x200 - ($-$$) - 1) db 0
db 0  ; checksum byte (fixed by a script)
