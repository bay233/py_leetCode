# 121. 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_i_0, dp_i_1 = 0, float('-INF')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
