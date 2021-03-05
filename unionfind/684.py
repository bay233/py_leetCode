# 684. 冗余连接

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        connected = {}

        def find(a):
            while connected.get(a) and a != connected.get(a):
                connected[a] = connected.get(connected[a], connected[a])
                a = connected[a]
            return a

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            connected[root_a] = root_b

        def is_connected(a, b):
            return find(a) == find(b)

        for edge in edges:
            x, y = edge[0], edge[1]
            if is_connected(x, y):
                res = edge
            else:
                union(x, y)
        return res


s = Solution()
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
