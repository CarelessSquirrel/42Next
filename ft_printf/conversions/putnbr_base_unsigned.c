#include "ft_printf.h"

int	print_unsigned_recursive(unsigned long n, int base, const char *digits)
{
	int		count;
	char	c;

	count = 0;
	if (n >= (unsigned long)base)
		count += print_unsigned_recursive(n / base, base, digits);
	c = digits[n % base];
	write(1, &c, 1);
	count++;
	return (count);
}
