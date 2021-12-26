# 807. 保持城市天际线

List = list


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_i, max_j = [], []
        n = len(grid)
        for i in range(n):
            max_i.append(max(grid[i]))
            t = 0
            for j in range(n):
                t = max(t, grid[j][i])
            max_j.append(t)

        res = 0
        for i in range(n):
            for j in range(n):
                res += min(max_i[i], max_j[j]) - grid[i][j]

        return res

s = Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))