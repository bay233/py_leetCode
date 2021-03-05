# 98. 验证二叉搜索树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.value = float('-INF')
        self.flag = True
        def do(root: TreeNode):
            if not root: return
            do(root.left)
            self.flag = self.flag and root.val > self.value
            if not self.flag:
                return
            self.value = root.val
            do(root.right)

        do(root)
        return self.flag


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(8)
right = root.right
right.right = TreeNode(10)
right.right.right = TreeNode(12)
right.right.right.right = TreeNode(14)

'''
        5
    1       8
                10
                    12
'''

s = Solution()
print(s.isValidBST(root))
