# 559. N 叉树的最大深度

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:

        def dp(node):
            if not node:
                return 0

            res = 1
            for n in node.children:
                res = max(res, dp(n) + 1)
            return res

        return dp(root)


s = Solution()
root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
print(s.maxDepth(root))
