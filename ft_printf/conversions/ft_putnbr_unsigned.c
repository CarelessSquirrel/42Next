#include "ft_printf.h"

int	ft_putnbr_unsigned(unsigned long n, int base, const char *digits)
{
	int		count;
	char	c;

	count = 0;
	if (n >= (unsigned long)base)
		count += ft_putnbr_unsigned(n / base, base, digits);
	c = digits[n % base];
	write(1, &c, 1);
	count++;
	return (count);
}
