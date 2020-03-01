# Binary Tree

* [Binary Tree Path](#binary-tree-path)
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

## Pre-order Traversal

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

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