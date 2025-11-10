/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 16:47:23 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/02 19:15:28 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include "libft.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_list
{
	int var;
	char **rand;
	struct s_list	*next;
}	t_list;

t_list	*ft_lstlast(t_list *lst)
{
	if (lst == NULL)
	{
		return (NULL);
	}
	while (lst->next != NULL)
	{
		lst = lst->next;
	}
	return (lst);
}

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i] != '\0')
	{
		i++;
	}
	return (i);
}

t_list	*ft_lstnew(int numb)
{
	t_list	*node;

	node = malloc(sizeof(t_list));
	if (node == NULL)
	{
		return (NULL);
	}
	node->var = numb;
	node->next = NULL;
	return (node);
}

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*last;

	if (new == NULL)
	{
		return ;
	}
	if (lst == NULL || *lst == NULL)
	{
		*lst = new;
		return ;
	}
	last = ft_lstlast(*lst);
	last->next = new;
}

int main(void)
{
	t_list *node1;
	t_list *head = NULL;

	node1 = ft_lstnew(4242);
	ft_lstadd_back(&head, node1);

	size_t i = sizeof(node1);
	
	//printf("%d\n", node1->var);
	
	printf("SizeOf:_%zu\n", sizeof(node1->var));

	// printf("%p\n", node1);

	// printf("%zu\n",i);
	return (0);
}