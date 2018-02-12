代码如下

	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	char buf[32];
	int main(int argc, char* argv[], char* envp[]){
		if(argc<2){
			printf("pass argv[1] a number\n");
			return 0;
		}
		int fd = atoi( argv[1] ) - 0x1234;
		int len = 0;
		len = read(fd, buf, 32);
		if(!strcmp("LETMEWIN\n", buf)){
			printf("good job :)\n");
			system("/bin/cat flag");
			exit(0);
		}
		printf("learn about Linux file IO\n");
		return 0;
	}

关键语句为

	int fd = atoi( argv[1] ) - 0x1234;

**0 号文件描述符是标准输入**，所以 argv[1]==0x1234 时就可以输入字符串 "LETMEWIN"。

输入下面的命令
	
	./fd 4660

再输入 LETMEWIN，就可以得到 flag
