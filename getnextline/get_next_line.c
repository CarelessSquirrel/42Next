/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 14:16:55 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/21 16:10:17 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>


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
		if (s1)
			free(s1);
		return (NULL);
	}
	if (s1)
		ft_memcpy(new_str, s1, len1);
	if (s2)
		ft_memcpy(new_str + len1, s2, len2);
	new_str[len1 + len2] = '\0';
	free(s1);
	return (new_str);
}

char	*get_next_line(int fd)
{
	static char	*remainder;
	int			bytes_read;
	char		*buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	
	
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return NULL;
	bytes_read = 1;
	while (!ft_strchr(remainder, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read < 0)
		{
			free(buffer);
			return NULL;
		}
		buffer[bytes_read] = '\0';
		remainder = join_free(remainder, buffer);
	}
	
}

int	main(void)
{
	int fd;
	char *next_line;
	int count;

	count = 0;
	fd = open("example.txt", O_RDONLY);
	if (fd == -1)
	{
		return (1);
	}
	while (1)
	{
		next_line = get_next_line(fd);
		if (next_line == NULL)
		{
			break;
		}
		count++;
		printf("%d: %s\n", count, next_line);
		free(next_line);
		next_line = NULL;
	}
	close (fd);
	return 0;
}