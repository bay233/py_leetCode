# 264. 丑数 II

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p_2, p_3, p_5 = 0, 0, 0
        for i in range(1, n):
            tmp = []
            dp_len = i
            if p_2 < dp_len:
                tmp.append(dp[p_2] * 2)
            if p_3 < dp_len:
                tmp.append(dp[p_3] * 3)
            if p_5 < dp_len:
                tmp.append(dp[p_5] * 5)
            dp.append(min(tmp))
            if dp[i] == 2 * dp[p_2]:
                p_2 += 1
            if dp[i] == 3 * dp[p_3]:
                p_3 += 1
            if dp[i] == 5 * dp[p_5]:
                p_5 += 1
        return dp[-1]

s = Solution()
print(s.nthUglyNumber(n = 10))
