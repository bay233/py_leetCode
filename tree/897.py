# 897. 递增顺序搜索树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dp(root):
            if not root: return []
            return dp(root.left) + [root.val] + dp(root.right)
        res = dp(root)
        head = TreeNode(res[0])
        res_root = head
        for i in range(1, len(res)):
            res_root.right = TreeNode(res[i])
            res_root = res_root.right
        return head

