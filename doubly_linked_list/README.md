# Doubly Linked Lists

* [Flatten a Multilevel Doubly Linked List](#flatten-a-multilevel-doubly-linked-list)

## Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their
own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first
level of the list.

Example:

Input: 1 = 2 = 3 =|= 6 = 7
                  4 = 5 
            
Output: 1 = 2 = 3 = 4 = 5 = 6 = 7

Iterative solution:

Time: O(N), Space: (N)

```python
def flatten_iterative(head: Node) -> Node:
    if not head:
        return head

    dummy = Node(0, None, head, None)
    previous = dummy

    stack = list()
    stack.append(head)

    while stack:
        current = stack.pop()
        previous.next = current
        current.previous = previous

        if current.next:
            stack.append(current.next)

        if current.child:
            stack.append(current.child)
            current.child = None

        previous = current
    dummy.next.previous = None
    return dummy.next
```

Recursive solution

Time: O(N), Space: O(N)

```python
def flatten(head: Node) -> Node:
    if not head:
        return head

    current = head

    while current:
        if current.child:
            next_node = current.next
            new_list = flatten(current.child)
            current.child = None
            current.next = new_list
            new_list.previous = current

            new_list_end_node = new_list
            while new_list_end_node.next:
                new_list_end_node = new_list_end_node.next
            new_list_end_node.next = next_node
            if next_node:
                next_node.previous = new_list_end_node
            current = next_node
        else:
            current = current.next

    return head
```