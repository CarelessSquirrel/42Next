#include "ft_printf.h"

int	print_pointer(void *ptr)
{
	unsigned long	address;
	int				count;

	if (!ptr)
		return write(1, "(nil)", 5);
	address = (unsigned long)ptr;
	write(1, "0x", 2);
	count = 2 + ft_putnbr_unsigned(address, 16, "0123456789abcdef");
	return (count);
}
