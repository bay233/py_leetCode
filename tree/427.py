# 427. 建立四叉树

List = list


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dp(i, i1, j, j1):
            if i1 - i == 1:
                return Node(grid[i][j], 1, None, None, None, None)
            m_i, m_j = (i1 + i) // 2, (j1 + j) // 2
            n1 = dp(i, m_i, j, m_j)
            n2 = dp(i, m_i, m_j, j1)
            n3 = dp(m_i, i1, j, m_j)
            n4 = dp(m_i, i1, m_j, j1)
            if n1.isLeaf and n2.isLeaf and n3.isLeaf and n4.isLeaf\
                    and n1.val == n2.val == n3.val == n4.val:
                return Node(n1.val, 1, None, None, None, None)

            return Node(1, 0, n1, n2, n3, n4)

        return dp(0, n, 0, n)


def show(node):
    if not node:
        return

    print(node.val, " ", node.isLeaf)
    if not node.isLeaf:
        show(node.topLeft)
        show(node.topRight)
        show(node.bottomLeft)
        show(node.bottomRight)



s = Solution()
show(s.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))
