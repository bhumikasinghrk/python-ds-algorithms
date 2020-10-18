# Binary Tree

* [Binary Tree Path](#binary-tree-path)
* [In-order Traversal](#in-order-traversal)
* [Level-order Traversal](#)
* [Post-order Traversal](#post-order-traversal)
* [Pre-order Traversal](#pre-order-traversal)

## Binary Tree Path

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:

Input:
```
   1
 /   \
2     3
 \
  5
```
Output: `["1->2->5", "1->3"]`

Explanation: All root-to-leaf paths are: `1->2->5`, `1->3`

```python
def binary_tree_paths(root_node: TreeNode) -> str:
    paths = []
    if not root_node:
        return paths
    get_path(root_node, '', paths)
    return paths

def get_path(node: TreeNode, path: str, paths: []) -> str:
    if not node.left and not node.right:
        paths.append(path + str(node.val))
        return
    if node.left:
        get_path(node.left, path + str(node.val) + '->', paths)
    if node.right:
        get_path(node.right, path + str(node.val) + '->', paths)
```

## In-order Traversal

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

Example:

     1
    / \
   2   3
  / \
 4   5 
 
Output: [4, 2, 5, 1, 1]

In-order traversal recursively

```python
def inorder_traversal(root: TreeNode) -> List[int]:
    values = []

    if not root:
        return values

    if root.left:
        values.extend(inorder_traversal(root.left))
    values.append(root.val)

    if root.right:
        values.extend(inorder_traversal(root.right))

    return values
```

In-order traversal with stack

```python
def inorder_traversal_stack(root: TreeNode) -> List[int]:
    output = []
    stack = []
    current_node = root

    while current_node or len(stack) > 0:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        output.append(current_node.val)
        current_node = current_node.right

    return output
```

## Level-order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example:

    1
   / \
  2   3
    /   \
   4     5

`[
  [1],
  [2, 3],
  [4, 5]
]`

```python
def level_order_traversal(root: TreeNode) -> List[List[int]]:
    values = []

    if not root:
        return values

    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        values.append(level)

    return values
```

## Post-order Traversal

Algorithm Postorder(tree)
   1. Traverse the left subtree
   2. Traverse the right subtree
   3. Visit the root.

Example:

     1
    / \
   2   3
  / \
 4   5 
 
Output: [4, 5, 2, 3, 1]
   
Recursive Approach:

 ```python
def postorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    if root.left:
        values.extend(postorder_traversal_recursive(root.left))
    if root.right:
        values.extend(postorder_traversal_recursive(root.right))

    values.append(root.val)

    return values
```

Iterative Approach:

```python
def postorder_traversal_iterative(root: TreeNode) -> List[int]:
    values = []
    stack = []

    while root or stack:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        if stack and root.right == stack[-1]:
            stack[-1] = root
            root = root.right
        else:
            values.append(root.val)
            root = None

    return values
```

## Pre-order Traversal

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

Example:

     1
    / \
   2   3
  / \
 4   5 
 
Output: [1, 2, 4, 5, 3]

Iterative approach Time: O(N), Space: O(N)

```python
def preorder_traversal_iterative(root: TreeNode) -> List[int]:
    output = []

    if root is None:
        return output

    stack = [root]
    while stack:
        root_node = stack.pop()
        if root_node is not None:
            output.append(root_node.val)
        if root_node.right is not None:
            stack.append(root_node.right)
        if root_node.left is not None:
            stack.append(root_node.left)
    return output
```

Morris version. Time: O(N), Space: O(1)

```python
def preorder_traversal_morris(root: TreeNode) -> List[int]:
    node, output = root, []
    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor = predecessor.right

            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right

    return output
```

Time: O(N), Space: O(N)

```python
def preorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    values.append(root.val)

    if root.left:
        values.extend(preorder_traversal_recursive(root.left))
    if root.right:
        values.extend(preorder_traversal_recursive(root.right))
    return values
```