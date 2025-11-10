#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int	ft_printf(const char *format, ...);
int	handle_conversion(char c, va_list args);

int	print_char(char c);
int	print_string(char *s);
int	print_pointer(void *ptr);
int	print_decimal(int n);
int	print_unsigned(unsigned int n);
int	print_hex(unsigned int n, int uppercase);

int	print_unsigned_recursive(unsigned long n, int base, const char *digits);
int	print_hex_recursive(unsigned long n, int uppercase);

#endif
