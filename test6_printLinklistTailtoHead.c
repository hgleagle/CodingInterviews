/*
 * 输入一个链表，从尾到头打印链表每个节点的值。
 * 用栈实现更好,不建议下面这个实现
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct ListNode {
      int val;
      struct ListNode *next;
} ListNode_t;


void printListFromTailToHead(ListNode_t *head)
{
    ListNode_t *next_node = head;
    int length = 0;
    int i = 0;

    while (next_node != NULL) {
        next_node = next_node->next;
        length += 1;
    }

    int value[length];
    memset(value, 0, length);
    next_node = head;
    while (i < length) {
        value[i] = next_node->val;
        next_node = next_node->next;
        i++;
    }

    for (i = length - 1; i >= 0; i--) {
        printf("%d\n", value[i]);
    }
}

int main(void)
{
    ListNode_t *head, *node, *prev;
    int i;

    prev = NULL;
    head = NULL;
    for (i = 0; i < 10; i++) {
        node = (ListNode_t *)malloc(sizeof(ListNode_t));
        if (node == NULL) {
            break;
        }
        node->val = i;
        node->next = NULL;
        if (prev != NULL) {
            prev->next = node;
        }
        if (head == NULL) {
            head = node;
        }
        prev = node;
    }

    if (head != NULL) {
        printListFromTailToHead(head);
    }

    node = head;
    while (node) {
        prev = node;
        free(node);
        node = prev->next;
    }
}
