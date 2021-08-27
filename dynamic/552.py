# 552. 学生出勤记录 II

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * 3 for __ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    if j == 1 and k == 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][0]) % mod
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][1]) % mod
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][2]) % mod
                    if k != 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % mod
                    if k == 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][0]) % mod
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][1]) % mod
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][2]) % mod
        res = 0
        for j in range(2):
            for k in range(3):
                res += dp[-1][j][k]
                res %= mod

        return res


s = Solution()
print(s.checkRecord(2))
