# 700. 二叉搜索树中的搜索

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root
