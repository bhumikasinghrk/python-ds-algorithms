
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# Wikipedia: Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next
# node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and
# traversal.
class SinglyLinkedList(object):
    _head = None

    def __init__(self, head: Node = None) -> None:
        if head:
            self._head = head

    def allvalues(self) -> []:
        values = []
        node = self._head

        while node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(N)
    def append(self, node: Node) -> None:
        if not self._head:
            self._head = node
            return

        last_node = self._head

        while last_node:
            next_node = last_node.next_node

            if not next_node:
                break
            last_node = next_node

        last_node.next_node = node

    # O(N)
    def get(self, index: int = None) -> Node:
        if not index and not self._head:  # No index and head is null
            return None
        elif not index and self._head:    # No index but head is present
            return self._head
        elif index:                       # Index provided
            count = 0
            current_node = self._head

            while current_node:
                next_node = current_node.next_node
                count += 1

                if next_node and count == index:
                    return next_node
                if next_node:
                    current_node = next_node
                    continue
                break

        return None                       # Index not valid, return None

    # O(N)
    def insert(self, node: Node, index: int = None) -> bool:
        success = False

        if not index or index == 0:
            if not self._head:
                self._head = node
            else:
                node.next_node = self._head
                self._head = node
            success = True
        else:
            previous_node = self.get(index - 1)
            insert_node = previous_node.next_node

            if previous_node:
                node.next_node = insert_node
                previous_node.next_node = node
                success = True

        return success

    # O(N)
    def remove(self, index: int) -> Node:
        node = None

        if index == 0:
            if self._head:
                node = self._head
                self._head = self._head.next_node
        else:
            previous_node = self.get(index - 1)
            node = previous_node.next_node

            # If node_to_remove is not present the index was invalid and we can return False
            if previous_node and node:
                previous_node.next_node = node.next_node
        return node

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next_node

        return count