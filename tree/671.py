# 671. 二叉树中第二小的节点

from deserialize.deser import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        head_val = root.val
        self.res_min = float('inf')

        def dp(root):
            if not root: return
            if root.val > head_val:
                self.res_min = min(self.res_min, root.val)
            dp(root.left)
            dp(root.right)

        dp(root)
        return self.res_min if self.res_min != float('inf') else -1


c = Codec()

s = Solution()
print(s.findSecondMinimumValue(c.deserialize([1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1])))
