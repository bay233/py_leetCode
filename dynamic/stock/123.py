# 123. 买卖股票的最佳时机 III

class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        dp_i_1_0, dp_i_1_1 = 0, float('-INF')
        dp_i_2_0, dp_i_2_1 = 0, float('-INF')

        for i in range(len(prices)):
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            dp_i_1_1 = max(dp_i_1_1, - prices[i])

        return max(dp_i_1_0, dp_i_2_0)

    def _maxProfit(self, prices: list[int]) -> int:
        dp = [[] for _ in range(len(prices))]
        for dps in dp:
            for i in range(3):
                dps.append([0] * 2)
        for i in range(len(prices)):
            for k in [2, 1]:
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-INF')
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return max(dp[len(prices) - 1][2][0], dp[len(prices) - 1][1][0])


s = Solution()
print(s._maxProfit([1,2,3,4,5]))

