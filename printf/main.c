#include "ft_printf.h"
#include <stdio.h>

int main(void)
{
    int num = 42;
    unsigned int unum = 3000;
    char c = 'A';
    char *str = "Hello 42!";
    void *ptr = &num;

    // Test %c
    ft_printf("Character: %c\n", c);

    // Test %s
    ft_printf("String: %s\n", str);

    // Test %p
    ft_printf("Pointer: %p\n", ptr);

    // Test %d and %i
    ft_printf("Signed decimal: %d, %i\n", num, -num);

    // Test %u
    ft_printf("Unsigned: %u\n", unum);

    // Test %x and %X
    ft_printf("Hex lowercase: %x\n", unum);
    ft_printf("Hex uppercase: %X\n", unum);

    // Test %%
    ft_printf("Percent sign: %%\n");

    return 0;
}
