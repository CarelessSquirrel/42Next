#include "ft_printf.h"

int	print_unsigned(unsigned int n)
{
	return ft_putnbr_unsigned(n, 10, "0123456789");
}
