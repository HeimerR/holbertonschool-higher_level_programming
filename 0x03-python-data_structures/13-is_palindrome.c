#include "lists.h"
/**
* is_palindrome - frees a listint_t list
* @head: pointer to list to be freed
* Return: 1 if it is palidrome, 0 if it is not
*/
int is_palindrome(listint_t **head)
{
	int len = 0, len2 = 0;
	listint_t *h, *h2;

	h = *head;
	if (!h)
		return (1);
	while (h)
	{
		h = h->next;
		len2++;
	}
	h = *head;
	while (len2 > 1)
	{
		h2 = h;
		len = len2;
		while (len - 1)
		{
			h2 = h2->next;
			len--;
		}
		if (h->n != h2->n)
			return (0);
		len2 -= 2;
		h = h->next;
	}
	return (1);
}
