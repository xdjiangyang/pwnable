代码如下

	#include <stdio.h>
	#include <string.h>
	unsigned long hashcode = 0x21DD09EC;
	unsigned long check_password(const char* p){
		int* ip = (int*)p;
		int i;
		int res=0;
		for(i=0; i<5; i++){
			res += ip[i];
		}
		return res;
	}
	
	int main(int argc, char* argv[]){
		if(argc<2){
			printf("usage : %s [passcode]\n", argv[0]);
			return 0;
		}
		if(strlen(argv[1]) != 20){
			printf("passcode length should be 20 bytes\n");
			return 0;
		}
	
		if(hashcode == check_password( argv[1] )){
			system("/bin/cat flag");
			return 0;
		}
		else
			printf("wrong passcode.\n");
		return 0;
	}

关键是

	if(hashcode == check_password( argv[1] ))

解题思路是输入一个特别的不含 "\x00" 的字符串，将其按整形数相加得到 0x21DD09EC,可以按如下方式拆分 0x21DD09EC

	21       DD       09       EC
	00100001 11011101 00001001 11101100
	
	00000001 11010101 00000001 11100100   \x01 \xd5 \x01 \xe4
	00001000 00000010 00000010 00000010   \x02 \x02 \x02 \x08
	00001000 00000010 00000010 00000010   \x02 \x02 \x02 \x08
	00001000 00000010 00000010 00000010   \x02 \x02 \x02 \x08
	00001000 00000010 00000010 00000010   \x02 \x02 \x02 \x08

在 python 命令行下执行如下代码可以得到 flag
	
	a='\xe4\x01\xd5\x01\x02\x02\x02\x08\x02\x02\x02\x08\x02\x02\x02\x08\x02\x02\x02\x08'
	os.system('/home/col/col %s'%a)
