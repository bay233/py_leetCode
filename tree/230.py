# 230. 二叉搜索树中第K小的元素

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def recall(root:TreeNode):
            return recall(root.left) + [root.val] + recall(root.right) if root else []
        return recall(root)[k - 1]

