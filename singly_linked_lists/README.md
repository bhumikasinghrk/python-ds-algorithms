# Linked Lists

* [Detect Cycle](#detect-cycle)
* [Find Middle Node](#find-middle-node)
* [Intersection Two Linked Lists](#intersection-two-linked-lists)
* [Linked List Cycle](#linked-list-cycle)
* [Merge Two Sorted Lists](#)
* [Odd Even Linked List](#odd-even-linked-list)
* [Palindrome Linked List](#)
* [Remove Linked List Elements](#remove-linked-list-elements)
* [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
* [Reverse Linked List](#reverse-linked-list)

## Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: `(2 -> 4 -> 3) + (5 -> 6 -> 4)`
Output: `7 -> 0 -> 8`
Explanation: `342 + 465 = 807`

```python
    node1 = head1
    node2 = head2
    dummy_node = ListNode(0)
    result = dummy_node
    carry = 0
    while node1 or node2:
        val1 = 0
        val2 = 0
        if node1:
            val1 = node1.val
            node1 = node1.next
        if node2:
            val2 = node2.val
            node2 = node2.next

        total = val1 + val2 + carry
        carry = int(total / 10)
        result.next = ListNode(total % 10)
        result = result.next

    if carry > 0:
        result.next = ListNode(carry)

    return dummy_node.next
```

## Detect Cycle

Given a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

Solution with slow/fast

Time: O(N), Space: O(1)

```python
def detect_cycle(head: ListNode) -> Optional[ListNode]:
    # detect cycle
    if not head or not head.next:
        return None
    slow: ListNode = head
    fast: ListNode = head
    intersection: Optional[ListNode] = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    if not intersection:
        return intersection

    # detect intersection
    node = head
    while node != intersection:
        node = node.next
        intersection = intersection.next

    return intersection
```

Solution with set

Time: O(N), Space: O(1)

```python
def detect_cycle_with_set(head: ListNode) -> Optional[ListNode]:
    visited_nodes: Set[ListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
```

## Find Middle Node

Find the node that is before the middle node. 

Example:

```text
[1] = 1
[1, 2] = 1
[1, 2, 3] = 2
[1, 2, 3, 4] = 2
```

```python
def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

## Intersection Two Linked Lists

Find the node at which the intersection of two singly linked lists begins

Example:

a1 -> a2 -> a3 \
                -> c1 -> c2 -> c3
      b1 -> b2 /
      
Answer: c1

Solution using two pointers:

Time: O(N), Space: O(1)
      
```python
def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    if not head_a or not head_b:
        return None
    
    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a != node_b:
        node_a = node_a.next
        node_b = node_b.next

        if node_a is None and node_b is None:
            return None

        if node_a is None:
            node_a = head_b

        if node_b is None:
            node_b = head_a

    return node_a
```

Solution using Set (less optimal)

Time: O(N), Space: O(N)

```python
def get_intersection_node_with_set(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    nodes: Set[ListNode] = set()
    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a or node_b:
        if node_a:
            if node_a in nodes:
                return node_a
            nodes.add(node_a)
            node_a = node_a.next

        if node_b:
            if node_b in nodes:
                return node_b
            nodes.add(node_b)
            node_b = node_b.next

    return None
```

## Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

```python
# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    slow: ListNode = head
    fast: ListNode = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
```

Solution with set (less optimal)

```python
# Time: O(N), Space: O(N)
def has_cycle_with_set(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    node_set: Set[ListNode] = set()
    node: ListNode = head

    while node:
        if not node or node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False
```

## Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two lists.

Example:

Input: `1->2->4`, `1->3->4`

Output: `1->1->2->3->4->4`

```python
def merge_two_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    if not head1 and not head2:
        return None

    node1 = head1
    node2 = head2
    dummy_node = ListNode(0)
    current_node = dummy_node

    while node1 and node2:
        if node1.val <= node2.val:
            current_node.next = node1
            node1 = node1.next
        else:
            current_node.next = node2
            node2 = node2.next
        current_node = current_node.next

    if node1:
        current_node.next = node1
    if node2:
        current_node.next = node2

    return dummy_node.next
```

## Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: `1->2->3->4->5->NULL`
Output: `1->3->5->2->4->NULL`

Time: O(N), Space: O(1)

```python
def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

    return head
```

## Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: `1->2`
Output: `false`

Example 2:

Input: `1->2->2->1`
Output: `true`

Time: O(N), Space: O(1)

```python
def is_palindrome(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    # Find midway
    first_half_end = find_middle_node(head)

    # reverse second half
    second_half_head = reverse_linked_list(first_half_end.next)

    # first half should match second half
    palindrome = True
    first_pointer = head
    second_pointer = second_half_head
    
    while palindrome and second_pointer:
        if first_pointer.val != second_pointer.val:
            return False
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    # restore list
    first_half_end.next = reverse_linked_list(second_half_head)
    return palindrome
```

## Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  `1->2->6->3->4->5->6, val = 6`
Output: `1->2->3->4->5`

Time: O(N), Space: O(1)

```python
def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy_node: ListNode = ListNode(0)
    dummy_node.next = head

    previous: ListNode = dummy_node
    current: Optional[ListNode] = head

    while current:
        if current.val == val:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return dummy_node.next
```

## Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Time: O(N), Space: O(1)

```python
def remove_nth_from_end(head: ListNode, nth: int) -> Optional[ListNode]:
    dummy: ListNode = ListNode(0)
    dummy.next = head
    previous: ListNode = dummy
    lead: ListNode = dummy

    # Move lead forward
    for _ in range(nth + 1):
        lead = lead.next

    # Move through list until lead is None
    while lead:
        previous = previous.next
        lead = lead.next

    # Delete Node by relinking nodes or reassigning head
    previous.next = previous.next.next
    return dummy.next
```

## Reverse Linked List

Reverse a Singly Linked List.

Time: O(N), Space: O(1)

```python
def reverse_linked_list(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None
    previous: O = None

```

Solution using recursion

Time: O(N), Space: O(N)

```python
def reverse_linked_list_recursive(head: ListNode) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```