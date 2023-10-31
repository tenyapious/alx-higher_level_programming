#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert number in a linked list
 * @head: head of linked list
 * @number: number
 *
 * Return: head on new linked list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *tail;

	if (temp == NULL)
		return (NULL);

	while (temp->next != NULL)
	{
		if (number <= temp->next->n)
		{
			tail = temp->next;
			temp->next = NULL;
			add_nodeint_end(head, number);
			temp->next->next = tail;
			temp = NULL;
			tail = NULL;
			break;
		}
		temp = temp->next;
	}
	return (*head);
}
