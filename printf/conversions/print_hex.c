/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_hex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 18:27:17 by jabettin          #+#    #+#             */
/*   Updated: 2025/12/12 04:24:17 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_hex(unsigned int n, int uppercase)
{
	if (uppercase)
		return (ft_putnbr_unsigned(n, 16, "0123456789ABCDEF"));
	else
		return (ft_putnbr_unsigned(n, 16, "0123456789abcdef"));
}
