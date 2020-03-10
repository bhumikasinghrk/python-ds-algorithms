from typing import Optional


class Node:
    def __init__(self,
                 val: int,
                 previous_node: Optional['Node'],
                 next_node: Optional['Node'],
                 child_node: Optional['Node']):
        self.val: int = val
        self.previous: Optional['Node'] = previous_node
        self.next: Optional['Node'] = next_node
        self.child: Optional['Node'] = child_node


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
