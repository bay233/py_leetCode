# 797. 所有可能的路径

List = list


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def dp(node, path):
            if node == n - 1:
                res.append(path.copy())
            if not graph[node]:
                return
            for i in graph[node]:
                path.append(i)
                dp(i, path)
                path.pop()

        dp(0, [0])
        return res


s = Solution()
print(s.allPathsSourceTarget([[1,3],[2],[3],[]]))
