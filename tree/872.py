# 872. 叶子相似的树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def get_leaf(root):
            if not root: return []
            if root.left == None and root.right == None:
                return [root.val]
            return get_leaf(root.left) + get_leaf(root.right)

        leaf1 = get_leaf(root1)
        leaf2 = get_leaf(root2)
        return leaf1 == leaf2

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
s = Solution()
print(s.leafSimilar(root,root))