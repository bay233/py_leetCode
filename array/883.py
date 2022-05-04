# 883. 三维形体投影面积

List = list


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        z = 0
        x = [0] * 51
        y = [0] * 51
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x[i] = max(x[i], grid[i][j])
                y[j] = max(y[j], grid[i][j])
                if grid[i][j]:
                    z += 1

        return z + sum(x) + sum(y)


s = Solution()
print(s.projectionArea([[1,0],[0,2]]))
