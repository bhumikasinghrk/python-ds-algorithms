from data_structures.singlylinkedlist import *

empty_list = SinglyLinkedList()

one_node_list = SinglyLinkedList(Node(5))


def test_init():
    assert one_node_list.size() == 1
    assert one_node_list.get().data == 5


def test_init_none():
    assert not empty_list.get(0)
    assert empty_list.size() == 0


def test_allvalues():
    singly_linked_list = get_multi_node_list()
    assert singly_linked_list.allvalues() == [5, 2, 4, 1]


def test_append_empty():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(Node(1))
    assert singly_linked_list.size() == 1
    assert singly_linked_list.get(0).data == 1


def test_append():
    singly_linked_list = SinglyLinkedList(Node(3))
    singly_linked_list.append(Node(4))
    assert singly_linked_list.size() == 2
    assert singly_linked_list.get(0).data == 3
    assert singly_linked_list.get(1).data == 4


def test_get_empty():
    assert not empty_list.get()


def test_get_invalid():
    assert not get_multi_node_list().get(10)


def test_get_valid():
    assert get_multi_node_list().get(3).data == 1


def test_insert_empty():
    singly_linked_list = SinglyLinkedList()
    assert singly_linked_list.insert(Node(3))
    assert singly_linked_list.size() == 1
    assert singly_linked_list.get(0).data == 3


def test_insert_head():
    singly_linked_list = get_multi_node_list()
    node = Node(32)
    assert singly_linked_list.insert(node, 0)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(0) == node
    assert singly_linked_list.get(1).data == 5


def test_insert_middle():
    singly_linked_list = get_multi_node_list()
    node = Node(11)
    assert singly_linked_list.insert(node, 1)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(0).data == 5
    assert singly_linked_list.get(1) == node
    assert singly_linked_list.get(2).data == 2


def test_insert_tail():
    singly_linked_list = get_multi_node_list()
    node = Node(22)
    assert singly_linked_list.insert(node, 3)
    assert singly_linked_list.size() == 5
    assert singly_linked_list.get(3) == node
    assert singly_linked_list.get(4).data == 1

def test_remove_empty():
    singly_linked_list = SinglyLinkedList()
    assert not singly_linked_list.remove(0)

def test_remove():
    singly_linked_list = get_multi_node_list()
    node = singly_linked_list.remove(0)
    assert node.data == 5
    assert singly_linked_list.size() == 3

    node = singly_linked_list.remove(2)
    assert node.data == 1
    assert singly_linked_list.size() == 2

def test_size():
    assert empty_list.size() == 0
    assert one_node_list.size() == 1
    assert get_multi_node_list().size() == 4


# Helpers


def get_multi_node_list() -> SinglyLinkedList:
    multi_node_list = SinglyLinkedList(Node(5))
    multi_node_list.append(Node(2))
    multi_node_list.append(Node(4))
    multi_node_list.append(Node(1))
    return multi_node_list
