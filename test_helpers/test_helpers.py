from singly_linked_lists.list_node import ListNode


def get_list_values(head: ListNode):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values
