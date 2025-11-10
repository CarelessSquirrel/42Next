#include "ft_printf.h"

int	print_str(char *str)
{
	int	len;

	len = 0;
	if (str == NULL)
	{
		write(1, "(null)", 6);
		return (6);
	}
	while (str[len] != '\0')
	{
		len++;
	}
	write(1, str, len);
	return (len);
}
