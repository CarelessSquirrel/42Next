#include "printf.h"

int	print_str(char *str)
{
	int	len;

	len = 0;
	if (str == '\0')
	{
		write(1, "null", 4);
		return (4);
	}
	while (str[len] != '\0')
	{
		len++;
	}
	write(1, str, len);
	return (len);
}