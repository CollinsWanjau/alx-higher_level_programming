#include "lists.h"

void reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_Palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *temp = *head;
    listint_t *dup = NULL;
    if (*head == NULL && (*head)->next == NULL)
    {
        return (1);
    }
    while (1)
    {
        fast = fast->next->next;
        if (fast == NULL)
        {
            dup = slow->next;
            break;
        }
        if (!fast->next)
        {
            dup = slow->next->next;
            break;
        }
        slow = slow->next;
    }
    reverse_listint(&dup);
    while (dup != NULL && temp != NULL)
    {
        if (temp->n == dup->n)
        {
            dup = dup->next;
            temp = temp->next;
        }
        else
            return (0);
    }
    if (!dup)
        return (1);
    return (0);
}
