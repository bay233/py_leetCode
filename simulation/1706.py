# 1706. 球会落何处

List = list


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = []
        for i in range(m):
            x, y = 0, i
            while x < n:
                ny = y + grid[x][y]
                if ny < 0 or ny >= m or grid[x][y] + grid[x][ny] == 0:
                    ans.append(-1)
                    break
                nx = x + 1
                if nx >= n:
                    ans.append(ny)
                    break
                x, y = nx, ny
        return ans


s = Solution()
print(s.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
