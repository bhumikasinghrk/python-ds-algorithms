from typing import Dict


class MapSum:
    def __init__(self):
        self.value = 0
        self.head: MapSumNode = MapSumNode()

    def insert(self, key: str, val: int) -> None:
        current_node = self.head
        for index in range(1, len(key) + 1):
            if key[:index] in current_node.nodes:
                current_node = current_node.nodes.get(key[:index])
            else:
                current_node.nodes.setdefault(key[:index], MapSumNode())
                current_node = current_node.nodes.get(key[:index])
        current_node.value = val

    def sum(self, prefix: str) -> int:
        current_node = self.head
        # Find target node
        for index in range(1, len(prefix) + 1):
            if prefix[:index] in current_node.nodes:
                current_node = current_node.nodes.get(prefix[:index])
            else:
                return 0

        # sum child nodes
        return self.__recursive_sum(current_node)

    def __recursive_sum(self, parent_node) -> int:
        if len(parent_node.nodes) == 0:
            return parent_node.value

        total = parent_node.value

        for node in parent_node.nodes:
            total += self.__recursive_sum(parent_node.nodes.get(node))
        return total


class MapSumNode:
    def __init__(self, value: int = 0):
        self.value = value
        self.nodes: Dict[str: MapSumNode] = dict()
