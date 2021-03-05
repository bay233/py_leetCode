# 111. 二叉树的最小深度

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        q = [[root]]
        step = 1

        while len(q) > 0:
            nodes = q.pop(0)
            qs = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return step
                if not node.left is None:
                    qs.append(node.left)
                if not node.right is None:
                    qs.append(node.right)
            q.append(qs)
            step += 1

        return step