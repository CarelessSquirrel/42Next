/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_conversion.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 18:26:58 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/10 18:26:59 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_conversion(char c, va_list args)
{
	int	count;

	count = 0;
	if (c == 'c')
		count += print_char(va_arg(args, int));
	else if (c == 's')
		count += print_str(va_arg(args, char *));
	else if (c == 'p')
		count += print_pointer(va_arg(args, void *));
	else if (c == 'd' || c == 'i')
		count += print_decimal(va_arg(args, int));
	else if (c == 'u')
		count += print_unsigned(va_arg(args, unsigned int));
	else if (c == 'x')
		count += print_hex(va_arg(args, unsigned int), 0);
	else if (c == 'X')
		count += print_hex(va_arg(args, unsigned int), 1);
	else if (c == '%')
		count += write(1, "%", 1);
	else
		count += write(1, &c, 1);
	return (count);
}
