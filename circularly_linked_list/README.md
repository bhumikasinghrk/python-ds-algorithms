# Circularly Linked Lists

* [Insert into a Cyclic Sorted List](#insert-into-a-cyclic-sorted-list)

## Insert into a Cyclic Sorted List

Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value 
into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the
list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the
insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference
to that single node. Otherwise, you should return the original given node.

```python
def insert(head: Optional[ListNode], value: int) -> Optional[ListNode]:
    if not head:
        cyclic_list = ListNode(value)
        cyclic_list.next = cyclic_list
        return cyclic_list

    previous = head
    node = head.next

    while node:
        if previous.val <= value <= node.val:
            new_node = ListNode(value)
            previous.next = new_node
            new_node.next = node
            return head
        if previous.val > node.val:
            if value >= previous.val or value <= node.val:
                new_node = ListNode(value)
                previous.next = new_node
                new_node.next = node
                return head

        previous = node
        node = node.next

        if previous == head:
            break

    new_node = ListNode(value)
    previous.next = new_node
    new_node.next = node

    return head
```
