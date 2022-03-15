# 1020. 飞地的数量

List = list


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        book = [[0] * m for _ in range(n)]
        q = []
        for i in range(n):
            if grid[i][0] == 1:
                q.append([i, 0])
                book[i][0] = 1
            if grid[i][m - 1] == 1:
                q.append([i, m - 1])
                book[i][m - 1] = 1

        for i in range(m):
            if grid[0][i] == 1:
                q.append([0, i])
                book[0][i] = 1
            if grid[n - 1][i] == 1:
                q.append([n - 1, i])
                book[n - 1][i] = 1

        step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            node = q.pop(0)
            x, y = node[0], node[1]
            for s in step:
                nx, ny = x + s[0], y + s[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or book[nx][ny]:
                    continue
                if grid[nx][ny] == 1:
                    book[nx][ny] = 1
                    q.append([nx, ny])
        ans = 0
        for i in range(n):
            for j in range(m):
                if book[i][j] != grid[i][j]:
                    ans += 1
        return ans

s = Solution()
print(s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],
                     [1,1,0,0,0,1,0,1,1,1],
                     [0,0,0,1,1,1,0,1,0,0],
                     [0,1,1,0,0,0,1,0,1,0],
                     [0,1,1,1,1,1,0,0,1,0],
                     [0,0,1,0,1,1,1,1,0,1],
                     [0,1,1,0,0,0,1,1,1,1],
                     [0,0,1,0,0,1,0,1,0,1],
                     [1,0,1,0,1,1,0,0,0,0],
                     [0,0,0,0,1,1,0,0,0,1]]))






