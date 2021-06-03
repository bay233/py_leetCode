# 1269. 停在原地的方案数

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        book = {}
        def dp(steps, arrlen, i):
            if steps == 0 and i == 0: return 1
            if steps < 0: return 0
            if (steps, i) in book: return book[(steps, i)]
            res = 0
            if i + 1 < arrlen:
                res += dp(steps - 1, arrlen, i + 1)
            if i - 1 >= 0:
                res += dp(steps - 1, arrlen, i - 1)
            res += dp(steps - 1, arrlen, i)
            book[(steps, i)] = res
            return res
        return dp(steps, arrLen, 0) % (10**9 + 7)

s = Solution()
print(s.numWays(3,2))