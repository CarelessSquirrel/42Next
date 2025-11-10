#include "ft_printf.h"

int	print_unsigned(unsigned int n)
{
	return print_unsigned_recursive(n, 10, "0123456789");
}
