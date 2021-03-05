import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.res = -2147483648
        def oneSideMax(root: TreeNode):
            if (root is None):
                return 0
            left = max(0, self.maxPathSum(root.left))
            right = max(0, self.maxPathSum(root.right))
            self.res = max(self.res, left + right + root.val)
            return max(left, right) + root.val

        oneSideMax(root)
        return self.res