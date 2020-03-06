from data_structures.circularly_linked_list import CircularlyLinkedList, Node

EMPTY_LIST = CircularlyLinkedList()
ONE_NODE_LIST = CircularlyLinkedList(Node(1))
MULTI_NODE_LIST = CircularlyLinkedList(Node(1))
MULTI_NODE_LIST.append(Node(2))
MULTI_NODE_LIST.append(Node(3))


def test_init():
    assert EMPTY_LIST.size() == 0
    assert EMPTY_LIST.all_values() == []
    assert ONE_NODE_LIST.size() == 1
    assert ONE_NODE_LIST.all_values() == [1]


def test_tail():
    assert not EMPTY_LIST.head
    assert ONE_NODE_LIST.head
    test_list = CircularlyLinkedList()
    test_list.head = Node(1)
    assert test_list.size() == 1


def test_all_values():
    assert EMPTY_LIST.all_values() == []
    assert ONE_NODE_LIST.all_values() == [1]
    assert MULTI_NODE_LIST.all_values() == [1, 2, 3]


def test_append():
    test_list = CircularlyLinkedList()
    test_list.append(Node(1))
    assert test_list.all_values() == [1]

    test_list.append(Node(2))
    assert test_list.all_values() == [1, 2]

    test_list.append(Node(3))
    assert test_list.all_values() == [1, 2, 3]


def test_remove():
    test_list = CircularlyLinkedList()
    test_list.append(Node(1))
    test_list.append(Node(2))
    test_list.append(Node(3))
    test_list.append(Node(4))

    test_list.remove(3)
    assert test_list.all_values() == [1, 2, 3]

    test_list.remove(1)
    assert test_list.all_values() == [1, 3]

    test_list.remove(0)
    assert test_list.all_values() == [3]

    test_list.remove(0)
    assert test_list.all_values() == []


def test_size():
    assert EMPTY_LIST.size() == 0
    assert ONE_NODE_LIST.size() == 1
    assert MULTI_NODE_LIST.size() == 3
