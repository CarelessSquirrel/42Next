/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:16:46 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/02 14:07:44 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdint.h>

void	*ft_calloc(size_t nmemb, size_t size)
{
	size_t			total_size;
	unsigned char	*p;

	if (nmemb == 0 || size == 0)
	{
		return (malloc(1));
	}
	if (nmemb > SIZE_MAX / size)
	{
		return (NULL);
	}
	total_size = nmemb * size;
	p = malloc(sizeof(*p) * (total_size));
	if (!p)
	{
		return (NULL);
	}
	ft_memset(p, 0, total_size);
	return ((void *)p);
}
