#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);
	newnode->n = number;

	while (current)
	{
		if (!current->next)
			break;
		if (current->next->n > number)
			break;
		current = current->next;
	}
	newnode->next = current->next;
	current->next = newnode;
}
