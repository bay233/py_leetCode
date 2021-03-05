# 222. 完全二叉树的节点个数

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0