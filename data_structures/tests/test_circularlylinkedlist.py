from data_structures.circularlylinkedlist import *

empty_list = CircularlyLinkedList()
one_node_list = CircularlyLinkedList(Node(1))
multi_node_list = CircularlyLinkedList(Node(1))
multi_node_list.append(Node(2))
multi_node_list.append(Node(3))


def test_init():
    assert empty_list.size() == 0
    assert empty_list.all_values() == []
    assert one_node_list.size() == 1
    assert one_node_list.all_values() == [1]


def test_tail():
    assert not empty_list.head
    assert one_node_list.head
    test_list = CircularlyLinkedList()
    test_list.head = Node(1)
    assert test_list.size() == 1


def test_all_values():
    assert empty_list.all_values() == []
    assert one_node_list.all_values() == [1]
    assert multi_node_list.all_values() == [1, 2, 3]


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
    assert empty_list.size() == 0
    assert one_node_list.size() == 1
    assert multi_node_list.size() == 3
