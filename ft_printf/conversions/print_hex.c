#include "ft_printf.h"

int print_hex(unsigned int n, int uppercase)
{
	if (uppercase)
		return ft_putnbr_unsigned(n, 16, "0123456789ABCDEF");
	else
		return ft_putnbr_unsigned(n, 16, "0123456789abcdef");
}
