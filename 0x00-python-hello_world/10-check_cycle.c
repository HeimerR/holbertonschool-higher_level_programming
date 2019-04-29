#include "lists.h"
/**
 * check_cycle - finds loops inside lists
 * @list: address pointer head
 * Return: 0 no loop, 1 loop
 */
int check_cycle(listint_t *list)
{
	listint_t *pslow, *pfast;

	if (list)
	{
		pslow = list->next;
		pfast = list->next->next;
		while (pslow && pfast)
		{
			if (pslow == pfast)
			{
				pslow = list;
				return (1);
			}
		pslow = pslow->next;
		pfast = pfast->next->next;
		}
	}
return (0);
}
