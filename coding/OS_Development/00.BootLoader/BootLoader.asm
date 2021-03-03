[ORG 0x00]			; start code and setting adress
[BITS 16]			; setting code 16bit

SECTION .text		; text section

jmp $				; loop start

times 510 - ( $ - $$ )	db	0x00		; $: line adress
										; $$: .txet start adress
										; $ - $$: offset
										; 510 - ( $ - $$ ): first adress ~ 510 adress
										; db	0x00: declaration 1byte, data is 0x00
										; time: loop
										; now adress from 510 adress insert 0x00
db 0x55				; declaration 1byte, data is 0x55
db 0xAA				; declaration 1byte, data is 0xAA
					; adress 511, 512 insert data 0x55, 0xAA (the boot secter)
