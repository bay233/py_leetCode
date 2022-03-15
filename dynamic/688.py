# 688. 骑士在棋盘上的概率

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        step = [[-1, -2], [-1, 2], [1, -2], [1, 2], [-2, 1], [-2, -1], [2, 1], [2, -1]]

        f = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                f[i][j][0] = 1

        for p in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for s in step:
                        nx, ny = i + s[0], j + s[1]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        f[i][j][p] += f[nx][ny][p - 1] / 8

        return f[row][column][k]

s = Solution()
print(s.knightProbability( 1,1,0,0))

