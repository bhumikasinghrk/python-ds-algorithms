from data_structures.singlylinkedlist import SinglyLinkedList, Node

EMPTY_LIST = SinglyLinkedList()
ONE_NODE_LIST = SinglyLinkedList(Node(5))


def test_init():
    assert ONE_NODE_LIST.size() == 1
    assert ONE_NODE_LIST.get(0) == 5


def test_init_none():
    assert not EMPTY_LIST.get(0)
    assert EMPTY_LIST.size() == 0


def test_all_values():
    singly_linked_list = get_multi_node_list()
    assert singly_linked_list.all_values() == [5, 2, 4, 1]


def test_append_empty():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(Node(1))
    assert singly_linked_list.size() == 1
    assert singly_linked_list.get(0) == 1


def test_append():
    singly_linked_list = SinglyLinkedList(Node(3))
    singly_linked_list.append(Node(4))
    assert singly_linked_list.size() == 2
    assert singly_linked_list.get(0) == 3
    assert singly_linked_list.get(1) == 4


def test_get_empty():
    assert not EMPTY_LIST.get(0)


def test_get_invalid():
    assert not get_multi_node_list().get(10)


def test_get_valid():
    assert get_multi_node_list().get(3) == 1


def test_get_node():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert(Node(3), 0)
    assert singly_linked_list.get_node(0).data == 3


def test_insert_empty():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert(Node(3), 0)
    assert singly_linked_list.size() == 1
    assert singly_linked_list.get(0) == 3


def test_insert_head():
    singly_linked_list = get_multi_node_list()
    singly_linked_list.insert(Node(32), 0)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(0) == 32
    assert singly_linked_list.get(1) == 5


def test_insert_middle():
    singly_linked_list = get_multi_node_list()
    singly_linked_list.insert(Node(11), 1)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(0) == 5
    assert singly_linked_list.get(1) == 11
    assert singly_linked_list.get(2) == 2


def test_insert_tail():
    singly_linked_list = get_multi_node_list()
    singly_linked_list.insert(Node(22), 3)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(3) == 22
    assert singly_linked_list.get(4) == 1


def test_remove_empty():
    singly_linked_list = SinglyLinkedList()
    assert not singly_linked_list.remove(0)


def test_remove():
    singly_linked_list = get_multi_node_list()
    assert singly_linked_list.remove(0) == 5
    assert singly_linked_list.size() == 3

    assert singly_linked_list.remove(2) == 1
    assert singly_linked_list.size() == 2


def test_size():
    assert EMPTY_LIST.size() == 0
    assert ONE_NODE_LIST.size() == 1
    assert get_multi_node_list().size() == 4


# Helpers


def get_multi_node_list() -> SinglyLinkedList:
    multi_node_list = SinglyLinkedList(Node(5))
    multi_node_list.append(Node(2))
    multi_node_list.append(Node(4))
    multi_node_list.append(Node(1))
    return multi_node_list
