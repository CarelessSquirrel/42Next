/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 15:13:41 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/12 17:44:16 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

char	*ft_strjoin(char *s1, char *s2)
{
	int		len1;
	int		len2;
	char	*new_str;

	if (!s1 || !s2)
		return NULL;
	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	new_str = malloc(sizeof(*new_str) * (len1 + len2 + 1));
	ft_memcpy(new_str, s1, len1);
	ft_memcpy(new_str + len1, s2, len2);
	return (new_str);
}

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

	if (!dest || !src)
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

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*sub;
	size_t	str_len;
	size_t	sub_len;

	if (!s)
		return (NULL);
	str_len = ft_strlen(s);
	if ((size_t)start >= str_len)
		return ;
	sub_len = str_len - (size_t)start;
	if (sub_len > len)
		sub_len = len;
	sub = malloc(sizeof(*sub) * (sub_len + 1));
	if (!sub)
		return (NULL);
	ft_memcpy(sub, s + start, sub_len);
	sub[sub_len] = '\0';
	return (sub);
}
int main(void)
{
	char	*str1 = "hello";
	char	*str2 = "world";
	char	*result = ft_strjoin(str1, str2);
	printf("%s", result);
}

