#include "printf.h"

int print_pointer(void *ptr)
{
	unsigned long address;
	int count;

	if (!ptr)
		return write(1, "null", 4);
	address = (unsigned long)ptr;
	write(1, "0x", 2);
	count = 2 + print_hex_recursive(address, 0);
	return count;
}

static int	print_hex_recursive(unsigned long n, int uppercase)
{
	char	*base;
	int		count;
	char	c;

	count = 0;
	if (uppercase)
	{
		base = "0123456789ABCDEF";
	}
	else 
	{
		base = "0123456789abcdef";
	}
	if (n >= 16)
		count += print_hex_recursive(n / 16, uppercase);
	c = base[n % 16];
	write(1, &c, 1);
	count++;
	return (count);
}
