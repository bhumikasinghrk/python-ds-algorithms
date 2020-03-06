from data_structures.doubly_linked_list import DoublyLinkedList


def test_init():
    linked_list = DoublyLinkedList()
    linked_list.append(3)
    assert linked_list.size() == 1
    assert linked_list.get(0) == 3


def test_init_none():
    assert not DoublyLinkedList().get(0)
    assert DoublyLinkedList().size() == 0


def test_all_values():
    doubly_linked_list = get_multi_node_list()
    assert doubly_linked_list.all_values() == [5, 2, 4, 1]


def test_append_empty():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    assert doubly_linked_list.size() == 1
    assert doubly_linked_list.get(0) == 1


def test_append():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    assert doubly_linked_list.size() == 2
    assert doubly_linked_list.get(0) == 3
    assert doubly_linked_list.get(1) == 4


def test_get_value():
    assert not DoublyLinkedList().get(0)
    assert not get_multi_node_list().get(10)
    assert get_multi_node_list().get(3) == 1


def test_get_node():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(3, 0)
    assert doubly_linked_list.get_node(0).data == 3


def test_insert_empty():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(3, 0)
    assert doubly_linked_list.size() == 1
    assert doubly_linked_list.get(0) == 3


def test_insert_head():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(32, 0)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.all_values() == [32, 5, 2, 4, 1]


def test_insert_middle():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(11, 1)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.all_values() == [5, 11, 2, 4, 1]


def test_insert_tail():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(22, 3)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.get(3) == 22
    assert doubly_linked_list.get(4) == 1


def test_remove_empty():
    doubly_linked_list = DoublyLinkedList()
    assert not doubly_linked_list.remove(0)


def test_remove():
    doubly_linked_list = get_multi_node_list()
    assert doubly_linked_list.remove(0) == 5
    assert doubly_linked_list.size() == 3

    assert doubly_linked_list.remove(2) == 1
    assert doubly_linked_list.size() == 2


def test_size():
    linked_list = DoublyLinkedList()
    assert linked_list.size() == 0

    linked_list.append(1)
    assert linked_list.size() == 1
    assert get_multi_node_list().size() == 4


# Helpers


def get_multi_node_list() -> DoublyLinkedList:
    multi_node_list = DoublyLinkedList()
    multi_node_list.append(5)
    multi_node_list.append(2)
    multi_node_list.append(4)
    multi_node_list.append(1)
    return multi_node_list
