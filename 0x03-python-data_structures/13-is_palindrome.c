#include "lists.h"
/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the pointer of the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the pointer of the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reversed = NULL;

	while (current)
	{
		add_nodeint_end(&reversed, current->n);
		current = current->next;
	}

	reverse_listint(&reversed);

	listint_t *first = *head;
	listint_t *second = reversed;
	int result = 1; /* Start with the assumption that it's a palindrome */

	while (first && second)
	{
		if (first->n != second->n)
		{
			result = 0;
			break;
		}
		first = first->next;
		second = second->next;
	}

	while (reversed)
	{
		listint_t *temp = reversed;
		reversed = reversed->next;
		free(temp);
	}

	return result;
}
