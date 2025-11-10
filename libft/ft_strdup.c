/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 15:54:24 by jabettin          #+#    #+#             */
/*   Updated: 2025/10/28 17:59:12 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*duplicate;
	char	*p;
	size_t	len;

	len = ft_strlen(s);
	duplicate = malloc(sizeof(*duplicate) * (len + 1));
	if (!duplicate)
	{
		return (NULL);
	}
	p = duplicate;
	while (*s)
	{
		*p++ = *s++;
	}
	*p = '\0';
	return (duplicate);
}
