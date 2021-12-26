# 375. 猜数字大小 II

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        book = [[0] * (n + 1) for _ in range(n + 1)]

        def dp(l, r):
            if r <= l: return 0
            if book[l][r] > 0: return book[l][r]
            ans = 0x3f3f3f3f
            for x in range(l, r + 1):
                cur = max(dp(l, x - 1), dp(x + 1, r)) + x
                ans = min(ans, cur)
            book[l][r] = ans
            return ans

        dp(1, n)
        return book[1][n]


s = Solution()
print(s.getMoneyAmount(1))
