# 236. 二叉树的最近公共祖先

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def do ( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if not root: return root
            left = do(root.left, p, q)
            right = do(root.right, p, q)
            if p.val == root.val or q.val == root.val:
                return root
            if left and right:
                return root
            return left if left else right
        return do(root, p, q)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(8)
right = root.right
right.right = TreeNode(10)
right.right.right = TreeNode(12)
right.right.right.right = TreeNode(14)


s = Solution()
print(s.lowestCommonAncestor(root, root.right, right.right.right.right).val)