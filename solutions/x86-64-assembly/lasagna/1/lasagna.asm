section .text
oven_time equ 40

global expected_minutes_in_oven
expected_minutes_in_oven:
    ; TODO: This function has no arguments
    mov rax, oven_time; and must return a number
    ret

global remaining_minutes_in_oven
remaining_minutes_in_oven:
    ; TODO: define the 'remaining_minutes_in_oven' function
    call expected_minutes_in_oven 
    sub rax, rdi; This function takes one number as argument and must return a number
    ret

global preparation_time_in_minutes
preparation_time_in_minutes:
    ; TODO: define the 'preparation_time_in_minutes' function
    mov rax, rdi
    imul rax, 2 ; This function takes one number as argument and must return a number
    ret

global elapsed_time_in_minutes
elapsed_time_in_minutes:
    ; TODO: define the 'elapsed_time_in_minutes' function
    mov rax, rdi
call preparation_time_in_minutes
    add rax, rsi ; This function takes two numbers as arguments and must return a number
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
