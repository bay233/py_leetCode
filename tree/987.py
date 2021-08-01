# 987. 二叉树的垂序遍历
import functools

from deserialize.deser import Codec

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    def verticalTraversal(self, root: TreeNode):
        book = collections.defaultdict(list)

        def dp(root, x, y):
            if not root: return
            book[y].append((x, root.val))
            dp(root.left, x + 1, y - 1)
            dp(root.right, x + 1, y + 1)

        dp(root, 0, 0)
        book_res = list(book.items())
        def key(a, b):
            if a[0] != b[0]: return a[0] - b[0]
            return a[1] - b[1]

        book_res.sort(key=lambda x: x[0])
        res = []
        for r in book_res:
            tmp = []
            sort_r1 = sorted(r[1], key=functools.cmp_to_key(key))
            for itm in sort_r1:
                tmp.append(itm[1])
            res.append(tmp)
        return res


s = Solution()
c = Codec()
print(s.verticalTraversal(c.deserialize([1,2,3,4,6,5,7])))
