# 802. 找到最终的安全状态

class Solution:
    # def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    def eventualSafeNodes(self, graph):
        book = [0] * len(graph)
        ne = [[] * len(graph) for i in range(len(graph))]
        for i in range(len(graph)):
            for val in graph[i]:
                book[i] += 1
                ne[val].append(i)

        q = []
        for i in range(len(book)):
            if book[i] == 0:
                q.append(i)
        while q:
            idx = q.pop(0)
            for i in ne[idx]:
                book[i] -= 1
                if book[i] == 0:
                    q.append(i)
        return [i for i in range(len(book)) if book[i] == 0]

s = Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))