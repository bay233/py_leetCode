# 122. 买卖股票的最佳时机 II

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_i_0, dp_i_1 = 0, float('-INF')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])

        return dp_i_0

    def _maxProfit(self, prices: list[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]

        for i in range(len(prices)):
            if i == 0:
                dp[i][1] = -prices[0]
                dp[i][0] = 0
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        print(dp)
        return dp[len(prices) - 1][0]


s = Solution()
print(s._maxProfit([7, 1, 5, 3, 6, 4]))
