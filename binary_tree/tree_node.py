from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
