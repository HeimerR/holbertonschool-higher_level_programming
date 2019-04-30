#include "lists.h"
/**
 * insert_node - inserts a new node sorted
 * @head: address new head
 * @number: number to insert
 * Return: head node’s data (n).
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *aux2;
	listint_t *new_node;
	unsigned int i = 0;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		printf("Error\n");
		return (0);
	}
	new_node->n = number;
	aux = *head;
	while (aux)
	{
		if (aux->n < number)
		{
			i++;
			aux2 = aux;
			aux = aux->next;
		}
		else
		{
			break;
		}
	}
	if (!i && !*head)
	{
		new_node->next = NULL;
	}
	if (!i)
	{
		new_node->next = *head;
		*head = new_node;
	return (new_node);
	}
	new_node->next = aux2->next;
	aux2->next = new_node;
	return (new_node);
}
