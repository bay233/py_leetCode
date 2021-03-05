# 322. 零钱兑换

class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != amount+1 else -1


    # def coinChange(self, coins: list[int], amount: int) -> int:
    #     memo = dict()
    #
    #     def dp(n):
    #         if n == 0: return 0
    #         if n < 0: return -1
    #         if n in memo: return memo[n]
    #         res = float('INF')
    #         for coin in coins:
    #             sub = dp(n - coin)
    #             if sub == -1: continue
    #             res = min(sub + 1, res)
    #
    #         memo[n] = res if res != float('INF') else -1
    #         return memo[n]
    #
    #     return dp(amount)