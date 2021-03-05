# 1319. 连通网络的操作次数

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        connected = {}

        def find(a):
            while connected.get(a) and a != connected.get(a):
                if connected.get(connected[a]):
                    connected[a] = connected.get(connected[a])
                a = connected[a]
            return a

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            connected[root_a] = root_b

        def is_connected(a, b):
            return find(a) == find(b)

        thread = 0
        for connection in connections:
            x, y = connection[0], connection[1]
            if is_connected(x, y):
                thread += 1
            else:
                union(x, y)

        use_thread = n - 1 - len(connected)
        return use_thread if thread >= use_thread else -1

s = Solution()
print(s.makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))