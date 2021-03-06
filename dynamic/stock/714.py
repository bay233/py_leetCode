# 714. 买卖股票的最佳时机含手续费

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp_i_0, dp_i_1 = 0, float('-INF')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)
        return dp_i_0

s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))