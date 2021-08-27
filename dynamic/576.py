# 576. 出界的路径数

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        book = {}
        paces = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dp(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if k <= 0: return 0
            if (x, y, k) in book: return book[(x, y, k)]
            ans = 0
            for pace in paces:
                ans += dp(x + pace[0], y + pace[1], k - 1)
                ans %= mod
            book[(x, y, k)] = ans
            return ans

        return dp(startRow, startColumn, maxMove)

s = Solution()
print(s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))