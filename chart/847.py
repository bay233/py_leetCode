# 847. 访问所有节点的最短路径

class Solution:
    # def shortestPathLength(self, graph: List[List[int]]) -> int:
    def shortestPathLength(self, graph) -> int:
        tar = 0
        q = []
        for i in range(len(graph)):
            tar = (tar << 1) | 1
            q.append((i, 1 << i))

        def dp(q, tar):
            step = 0
            while q:
                level = q.pop(0)
                tmp = []
                while level:
                    node = level.pop(0)
                    state = node[1]
                    if state == tar:
                        return step
                    for n in graph[node[0]]:
                        tmp.append((n, state | (1 << n)))
                q.append(tmp)
                step += 1
        return dp([q], tar)


s = Solution()
print(s.shortestPathLength([[1,5],[0,3],[3,5],[1,2,5],[7],[0,7,6,2,3],[5],[5,4,8],[7]]))






