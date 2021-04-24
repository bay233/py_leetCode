# 783. 二叉搜索树节点最小距离

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dp(root):
            if not root: return []
            return dp(root.left) + [root.val] + dp(root.right)

        tree_list = dp(root)
        res_min = float('inf')
        for i in range(1, len(tree_list)):
            res_min = min(res_min, tree_list[i] - tree_list[i - 1])
        return res_min

    def minDiffInBST2(self, root: TreeNode) -> int:
        self.a1 = None
        self.a2 = None
        self.res = float('inf')
        def dp(root):
            if not root: return
            dp(root.left)
            self.a1, self.a2 = self.a2, root.val
            if self.a1 != None and self.a2 != None:
                self.res = min(self.res, self.a2 - self.a1)
            dp(root.right)
        dp(root)
        return self.res

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)

s = Solution()
print(s.minDiffInBST2(root))