# 743. 网络延迟时间

from collections import defaultdict


class Solution:
    #  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        book = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for time in times:
            book[time[0]][time[1]] = time[2]
        for i in range(1, n + 1):
            book[i][i] = 0

        res = 0
        for m in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                        book[i][j] = min(book[i][j], book[i][m] + book[m][j])
        for i in range(1, n + 1):
            if book[k][i] == float('inf'):
                return -1
            res = max(book[k][i], res)
        return res

s = Solution()
print(s.networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3))
