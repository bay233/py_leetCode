# 563. 二叉树的坡度

from deserialize import deser


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res = 0

        def dp(node):
            if not node:
                return 0

            left = dp(node.left)
            right = dp(node.right)
            self.res += abs(left - right)
            return left + right + node.val

        dp(root)
        return self.res


s = Solution()
de = deser.Codec()
print(s.findTilt(de.deserialize([21, 7, 14, 1, 1, 2, 2, 3, 3])))
