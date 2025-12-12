/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 17:46:48 by jabettin          #+#    #+#             */
/*   Updated: 2025/12/12 04:32:18 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int	count_len(int n)
{
	int		len;
	long	num;

	len = 0;
	num = n;
	if (num <= 0)
		len++;
	while (num != 0)
	{
		num = num / 10;
		len++;
	}
	return (len);
}

static void	ft_putnbr(long n, char *str, int *index)
{
	char	c;

	if (n > 9)
	{
		ft_putnbr(n / 10, str, index);
	}
	c = n % 10 + '0';
	str[*index] = c;
	(*index)++;
}

char	*ft_itoa(int n)
{
	int		len;
	long	num;
	char	*str;
	int		i;

	len = count_len(n);
	num = n;
	i = 0;
	str = malloc(sizeof(*str) * (len + 1));
	if (!str)
		return (NULL);
	if (num < 0)
	{
		str[i] = '-';
		num = -num;
		i++;
	}
	ft_putnbr(num, str, &i);
	str[i] = '\0';
	return (str);
}

int	main(void)
{
	int i = -7 / 10;
	printf("SizeOf:_%d\n", i);

	// printf("%p\n", node1);

	// printf("%zu\n",i);
	return (0);
}
