# 965. 单值二叉树

import deserialize.deser as de

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        a, b = True, True
        if root.left:
            a = root.left.val == root.val and self.isUnivalTree(root.left)
        if root.right:
            b = root.right.val == root.val and self.isUnivalTree(root.right)
        return a and b

null = None
c = de.Codec()
s = Solution()
print(s.isUnivalTree(c.deserialize([9,9,6,9,9])))