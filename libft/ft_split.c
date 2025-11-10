/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 03:37:11 by jbetting          #+#    #+#             */
/*   Updated: 2025/10/29 03:59:18 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	word_count(const char *s, char c)
{
	int	count;

	count = 0;
	while (*s)
	{
		while (*s && *s == c)
			s++;
		if (*s && *s != c)
		{
			count++;
			while (*s && *s != c)
				s++;
		}
	}
	return (count);
}

static char	*word_place(const char *start, int len)
{
	char	*word;

	word = malloc(sizeof(*word) * (len + 1));
	if (!word)
		return (NULL);
	ft_memcpy(word, start, len);
	word[len] = '\0';
	return (word);
}

static char	*next_word(const char **s_ptr, char c)
{
	const char	*start;
	int			len;
	char		*word;

	len = 0;
	while (**s_ptr && **s_ptr == c)
		(*s_ptr)++;
	start = *s_ptr;
	while ((*s_ptr)[len] && (*s_ptr)[len] != c)
		len++;
	word = word_place(start, len);
	if (word)
		*s_ptr += len;
	return (word);
}

char	**ft_split(const char *s, char c)
{
	char	**result;
	int		i;
	int		wc;

	if (!s)
		return (NULL);
	wc = word_count(s, c);
	result = malloc(sizeof(*result) * (wc + 1));
	if (!result)
		return (NULL);
	i = 0;
	while (i < wc)
	{
		result[i] = next_word(&s, c);
		if (!result[i])
		{
			while (i > 0)
				free(result[--i]);
			free(result);
			return (NULL);
		}
		i++;
	}
	result[i] = NULL;
	return (result);
}
