# 938. 二叉搜索树的范围和

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dp(root):
            if not root: return 0
            res = 0
            res += dp(root.left)
            res += dp(root.right)
            if root.val < low: return res
            if root.val > high: return res
            return res + root.val

        return dp(root)


