# 653. 两数之和 IV - 输入 BST
from deserialize import deser as code


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k: int) -> bool:

        def dp(left, right):
            if not left or not right:
                return False
            v = left.val + right.val
            if v == k:
                if left == right:
                    return False
                return True
            elif v > k:
                return dp(left.left, right) or dp(left, right.left)
            else:
                return dp(left.right, right) or dp(left, right.right)

        ans = False
        if root.left:
            ans = ans or dp(root.left, root)
        if root.right:
            ans = ans or dp(root, root.right)
        return ans


null = None
c = code.Codec()
s = Solution()
print(s.findTarget(c.deserialize([2,null,3]), 6))
