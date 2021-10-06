# 650. 只有两个键的键盘

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [_ for _ in range(n + 1)]
        dp[1] = 0
        for i in range(2, (n + 1) // 2):
            if n % i: continue
            if i * 2 <= n:
                k = i * 2
                dp[k] = min(dp[k], dp[i] + 2)
                k_dp = dp[k]
                while k + i <= n:
                    idx = k + i
                    k_dp += 1
                    dp[idx] = min(dp[idx], k_dp)
                    k = idx

        return dp[-1]

s = Solution()
print(s.minSteps(741))
