# 863. 二叉树中所有距离为 K 的结点


from deserialize.deser import Codec


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ChartNode:
    def __init__(self, x):
        self.val = x
        self.next = []


class Solution:
    # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    N = 510
    M = N * 4

    def distanceK(self, root: TreeNode, t: TreeNode, k: int):
        he = [-1] * self.N
        e = [0] * self.M
        ne = [0] * self.M
        idx = 0
        vis = [False] * self.N

        def add(a, b):
            nonlocal idx
            e[idx] = b
            ne[idx] = he[a]
            he[a] = idx
            idx += 1

        def dfs(root):
            if not root:
                return
            if root.left:
                add(root.val, root.left.val)
                add(root.left.val, root.val)
                dfs(root.left)
            if root.right:
                add(root.val, root.right.val)
                add(root.right.val, root.val)
                dfs(root.right)

        def find(root, m, cur):
            if cur == m:
                ans.append(root)
                return
            i = he[root]
            while i != -1:
                j = e[i]
                if not vis[j]:
                    vis[j] = True
                    find(j, m, cur + 1)
                i = ne[i]

        ans = []
        dfs(root)
        vis[t.val] = True
        find(t.val, k, 0)
        return ans


c = Codec()
s = Solution()
print(s.distanceK(c.deserialize([0, 2, 1, None, None, 3]), TreeNode(3), 3))
