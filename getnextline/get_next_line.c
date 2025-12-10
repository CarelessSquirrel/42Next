/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 14:16:55 by jabettin          #+#    #+#             */
/*   Updated: 2025/12/10 17:40:54 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*join_free(char *s1, char *s2)
{
	char	*new_str;
	size_t	len1;
	size_t	len2;

	len1 = 0;
	len2 = 0;
	if (s1)
		len1 = ft_strlen(s1);
	if (s2)
		len2 = ft_strlen(s2);
	new_str = malloc(sizeof(*new_str) * (len1 + len2 + 1));
	if (!new_str)
	{
		return (free(s1), NULL);
	}
	if (s1)
		ft_memcpy(new_str, s1, len1);
	if (s2)
		ft_memcpy(new_str + len1, s2, len2);
	new_str[len1 + len2] = '\0';
	free(s1);
	return (new_str);
}

static char	*update_remainder(char *old, size_t start)
{
	char	*new;

	if (old[start] == '\0')
		return (free(old), NULL);
	new = ft_substr(old, start, ft_strlen(old) - start);
	free(old);
	return (new);
}

static char	*extract_line(char **remainder)
{
	char	*line;
	char	*nl_ptr;
	size_t	len;

	if (!*remainder)
		return (NULL);
	nl_ptr = ft_strchr(*remainder, '\n');
	if (nl_ptr)
	{
		len = nl_ptr - *remainder + 1;
		line = ft_substr(*remainder, 0, len);
		*remainder = update_remainder(*remainder, len);
		return (line);
	}
	line = ft_substr(*remainder, 0, ft_strlen(*remainder));
	free(*remainder);
	*remainder = NULL;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*remainder;
	char		*buffer;
	ssize_t		bytes_read;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	bytes_read = 1;
	while (bytes_read > 0 && (!remainder || !ft_strchr(remainder, '\n')))
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read < 0)
			return (free(buffer), free(remainder), remainder = NULL, NULL);
		buffer[bytes_read] = '\0';
		remainder = join_free(remainder, buffer);
		if (!remainder)
			return (free(buffer), remainder = NULL, NULL);
	}
	free(buffer);
	if (!remainder || !*remainder)
		return (free(remainder), remainder = NULL, NULL);
	return (extract_line(&remainder));
}
