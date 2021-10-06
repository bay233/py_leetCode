# 437. 路径总和 III


import deserialize.deser as de

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        book = [0]
        self.res = 0

        def dp(node):
            if not node: return
            book.append(book[-1] + node.val)
            tmp = book[-1]
            for b in book[:-1]:
                if tmp - b == targetSum:
                    self.res += 1
            dp(node.left)
            dp(node.right)
            book.pop()
        dp(root)
        return self.res


root = de.Codec().deserialize([5,4,8,11,None,13,4,7,2,None,None,5,1])
s = Solution()
print(s.pathSum(root, 22))