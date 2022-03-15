# 1765. 地图中的最高点


List = list


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        book = []
        n, m = len(isWater), len(isWater[0])
        step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = []
        for i in range(n):
            tmp = []
            for j in range(m):
                if isWater[i][j]:
                    tmp.append(0)
                    q.append((i, j))
                else:
                    tmp.append(-1)
            book.append(tmp)

        while q:
            point = q.pop(0)
            x, y = point[0], point[1]
            for s in step:
                nx, ny = x + s[0], y + s[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if book[nx][ny] != -1:
                    continue
                book[nx][ny] = book[x][y] + 1
                q.append((nx, ny))
        return book


s = Solution()
print(s.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
