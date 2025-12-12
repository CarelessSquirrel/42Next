/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_pointer.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 18:27:20 by jabettin          #+#    #+#             */
/*   Updated: 2025/12/12 04:22:04 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_pointer(void *ptr)
{
	unsigned long	address;
	int				count;

	if (!ptr)
		return (write(1, "(nil)", 5));
	address = (unsigned long)ptr;
	write(1, "0x", 2);
	count = 2 + ft_putnbr_unsigned(address, 16, "0123456789abcdef");
	return (count);
}
