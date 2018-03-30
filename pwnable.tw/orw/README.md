1. IDA 打开 orw 后发现，此程序接收一段读取 /home/orw/flag 的 shellcode 并执行。

2. 编写 orw_shellcode.asm，执行如下命令提取shellcode

	 	nasm -f elf orw_shellcode.asm -o orw_shellcode.o
		ld -s orw_shellcode.o -o orw_shellcode
		objdump -s orw_shellcode

3. 执行 get_flag.py 获取 flag