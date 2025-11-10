#include "ft_printf.h"

int	print_decimal(int n)
{
	long	nb;
	int		count;

	count = 0;
	nb = n;
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
		count++;
	}
	count += ft_putnbr_unsigned(nb, 10, "0123456789");
	return (count);
}
