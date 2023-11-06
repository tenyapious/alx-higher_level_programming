#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_len - get length of listint_t list
 * @head: pointer of first node of listint_t list
 *
 * Return: length of listint_t list
*/
int list_len(listint_t *head)
{
	listint_t *temp;
	int len = 0;

	temp = head;

	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}

	return (len);
}

/**
 * nnode_val - get value of a node at a position
 * @head: pointer of first node of listint_t list
 * @n: position of node
 *
 * Return: value of the node
*/
int nnode_val(listint_t *head, int n)
{
	listint_t *temp;

	temp = head;
	while (--n)
	{
		temp = temp->next;
	}

	return (temp->n);
}

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer of first node of listint_t list
 *
 * Return: 1 if true or 0 if false
*/
int is_palindrome(listint_t **head)
{
	int len, halflen, i, j;

	if (*head == NULL)
		return (1);

	len = list_len(*head);
	halflen = len / 2;

	for (i = 1, j = len ; i <= halflen; i++, j--)
	{
		if (nnode_val(*head, i) != nnode_val(*head, j))
			return (0);
	}

	return (1);
}
