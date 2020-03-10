from typing import Dict, Optional


class Node:
    def __init__(self, value: int, next_node: 'Node' = None, random: 'Node' = None):
        self.value = value
        self.next = next_node
        self.random = random


def copy_random_list(head: Node) -> Node:
    if not head:
        return None

    current = head
    nodes = {}
    new_node = Node(head.value, None, None)
    nodes[current] = new_node

    while current:
        new_node.random = get_cloned_node(current.random, nodes)
        new_node.next = get_cloned_node(current.next, nodes)
        current = current.next
        new_node = new_node.next

    return get_cloned_node(head, nodes)


def get_cloned_node(node: Node, visited: Dict) -> Optional[Node]:
    if node:
        if node in visited:
            return visited[node]
        visited[node] = Node(node.value, None, None)
        return visited[node]
    return None
