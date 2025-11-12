/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 14:16:55 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/12 14:07:31 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

char	*get_next_line(int fd)
{
	int	bytes_read;
	char	*buffer;
	
	buffer = malloc(sizeof(*buffer) * 5 + 1);
	if (!buffer)
	{
		return NULL;
	}
	bytes_read = read(fd, buffer, 5);
	if (bytes_read <= 0)
	{
		free(buffer);
		return NULL;
	}
	return buffer;
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