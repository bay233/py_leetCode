# 188. 买卖股票的最佳时机 IV

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [[] for _ in range(len(prices))]
        for dps in dp:
            for i in range(k + 1):
                dps.append([0] * 2)
        for i in range(len(prices)):
            for k1 in range(k, 0, -1):
                if i == 0:
                    dp[i][k1][0] = 0
                    dp[i][k1][1] = float('-INF')
                    if k1 == 1:
                        dp[i][k1][1] = -prices[i]
                    continue
                dp[i][k1][0] = max(dp[i - 1][k1][0], dp[i - 1][k1][1] + prices[i])
                dp[i][k1][1] = max(dp[i - 1][k1][1], dp[i - 1][k1 - 1][0] - prices[i])
        return max([k[0] for k in dp[len(prices) - 1]]) if len(prices) > 0 else 0


s = Solution()
print(s.maxProfit(2, []))
