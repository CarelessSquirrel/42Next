/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 15:13:41 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/21 15:33:42 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>


size_t	ft_strlen(char	*str)
{
	size_t	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*d;
	unsigned char	*s;

	d = (unsigned char *)dest;
	s = (unsigned char *)src;

	if (!dest && !src)
		return (NULL);
	while (n > 0)
	{
		*d = *s;
		d++;
		s++;
		n--;
	}
	return dest;
}

char	*ft_strchr(const char *s, int c)
{
	while (*s != '\0' && *s != (char)c)
	{
		s++;
	}
	if (*s == (char)c)
	{
		return ((char *)s);
	}
	return (NULL);
}

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	len;
	
	len = ft_strlen(s);
	dup = malloc(sizeof(*dup) * (len + 1));
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, len);
	*dup = '\0';
	return (dup);
}


int main(void)
{
	char	*str1 = "hello";
	char	*str2 = "world";
	char	*result = ft_strdup(str1);
	printf("%s", result);
}

