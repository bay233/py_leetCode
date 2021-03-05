# 114. 二叉树展开为链表

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Do not return anything, modify root in-place instead.
    """

    def flatten(self, root: TreeNode) -> None:
        if not root: return

        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None

        node = root
        while node.right:
            node = node.right
        node.right = tmp
