/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/02 15:16:29 by jabettin          #+#    #+#             */
/*   Updated: 2025/11/02 16:39:20 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*temp;
	t_list	*current;

	if (lst == NULL || *lst == NULL)
	{
		return ;
	}
	current = *lst;
	while (current != NULL)
	{
		temp = current->next;
		if (del != NULL)
		{
			del(current->content);
		}
		free(current);
		current = temp;
	}
	*lst = NULL;
}
