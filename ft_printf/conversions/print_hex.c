#include "printf.h"

int print_hex(unsigned int n, int uppercase)
{
	if (uppercase)
		return print_unsigned_recursive(n, 16, "0123456789ABCDEF");
	else
		return print_unsigned_recursive(n, 16, "0123456789abcdef");
}
