# 652. 寻找重复的子树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        trees = {}
        res = []
        def subtrees(root: TreeNode, tress, res):
            if not root: return "#"
            left = subtrees(root.left, tress, res)
            right = subtrees(root.right, tress, res)
            treeStr = str(root.val) + "." + left + "." + right
            if trees.get(treeStr) and trees.get(treeStr) == 1:
                res.append(root)
            trees[treeStr] = trees.get(treeStr, 0) + 1
            return treeStr

        subtrees(root, trees, res)
        return res


