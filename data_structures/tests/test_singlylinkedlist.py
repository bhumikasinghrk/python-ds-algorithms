from data_structures.singly_linked_list import SinglyLinkedList

EMPTY_LIST = SinglyLinkedList()


def test_init():
    linked_list = SinglyLinkedList()
    assert linked_list.size() == 0


def test_all_values():
    linked_list = get_multi_node_list()
    assert linked_list.all_values() == [1, 2, 3]


def test_append_empty():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    assert linked_list.size() == 1
    assert linked_list.get(0) == 1


def test_append():
    linked_list = SinglyLinkedList()
    linked_list.append(4)
    linked_list.append(5)
    assert linked_list.size() == 2
    assert linked_list.get(0) == 4
    assert linked_list.get(1) == 5


def test_get_empty():
    assert not SinglyLinkedList().get(0)


def test_get_invalid():
    assert not get_multi_node_list().get(10)


def test_get_valid():
    assert get_multi_node_list().get(2) == 3


def test_insert_empty():
    linked_list = SinglyLinkedList()
    linked_list.insert(3, 0)
    assert linked_list.size() == 1
    assert linked_list.get(0) == 3


def test_insert_head():
    linked_list = get_multi_node_list()
    linked_list.insert(32, 0)
    assert linked_list.size() == 4
    assert linked_list.get(0) == 32
    assert linked_list.get(1) == 1


def test_insert_middle():
    linked_list = get_multi_node_list()
    linked_list.insert(11, 1)
    assert linked_list.size() == 4
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 11
    assert linked_list.get(2) == 2


def test_insert_tail():
    linked_list = get_multi_node_list()
    linked_list.insert(22, 3)
    assert linked_list.size() == 4
    assert linked_list.get(3) == 22


def test_remove_empty():
    linked_list = SinglyLinkedList()
    assert not linked_list.remove(0)


def test_remove():
    linked_list = get_multi_node_list()
    linked_list.remove(0)
    assert linked_list.size() == 2

    linked_list.remove(1)
    assert linked_list.size() == 1


def test_size():
    assert SinglyLinkedList().size() == 0
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    assert linked_list.size() == 1
    assert get_multi_node_list().size() == 3


# Helpers


def get_multi_node_list() -> SinglyLinkedList:
    multi_node_list = SinglyLinkedList()
    multi_node_list.append(1)
    multi_node_list.append(2)
    multi_node_list.append(3)
    return multi_node_list
