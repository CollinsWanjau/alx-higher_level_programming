#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle in it
 * @list: pointer to a node
 *
 * Description:For optimal perfomance, this function
 * assumes that a circular linked list would circle back to the
 * head of the list (this is common in linked list implementation)
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!(fast && fast->next))
		return (0);

	slow = list->next;
	fast = fast->next->next;
	if (slow == list || fast == list || slow == fast)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
