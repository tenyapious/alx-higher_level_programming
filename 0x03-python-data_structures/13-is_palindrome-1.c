#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * dup_list - duplate a linked list
 * @head: pointer of first node of listint_t list
 *
 * Return: address of new list
*/
listint_t *dup_list(listint_t *head)
{
	listint_t *new_list, *temp;

	new_list = NULL;
	temp = head;

	while (temp != NULL)
	{
		add_nodeint_end(&new_list, temp->n);
		temp = temp->next;
	}

	return (new_list);
}

/**
 * reverse_list - reverse a linked list
 * @head: pointer of first node of listint_t list
 *
 * Return: address of the linked list
*/
listint_t *reverse_list(listint_t *head)
{
	listint_t *next_node, *temp;

	if (head == NULL)
		return (NULL);
	else if (head->next == NULL)
		return (head);

	next_node = head->next;
	temp = next_node->next;
	head->next = NULL;
	next_node->next = head;
	head = next_node;

	while (temp != NULL)
	{
		next_node = temp;
		temp = next_node->next;
		next_node->next = head;
		head = next_node;
	}

	return (head);
}

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer of first node of listint_t list
 *
 * Return: 1 if true or 0 if false
*/
int is_palindrome(listint_t **head)
{
	listint_t *h, *temp1, *temp2;
	int is_pal = 1;

	h = dup_list(*head);
	h = reverse_list(h);

	temp1 = *head;
	temp2 = h;

	while (temp1 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			is_pal = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	free_listint(h);
	return (is_pal);
}
