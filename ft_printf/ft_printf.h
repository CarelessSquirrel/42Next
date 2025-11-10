#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int	ft_printf(const char *format, ...);
int	handle_conversion(char c, va_list args);

int	print_char(int c);
int	print_str(char *s);
int	print_pointer(void *ptr);
int	print_decimal(int n);
int	print_unsigned(unsigned int n);
int	print_hex(unsigned int n, int uppercase);

int	ft_putnbr_unsigned(unsigned long n, int base, const char *digits);

#endif
