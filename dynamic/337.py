# 337. 打家劫舍 III

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root: TreeNode):
            if not root: return 0, 0
            left = dp(root.left)
            right = dp(root.right)
            rob = root.val + left[0] + right[0]
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            return not_rob, rob

        return max(dp(root))


# [2,1,3,null,4]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

s = Solution()
print(s.rob(root))
