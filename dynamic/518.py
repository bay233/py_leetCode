# 518. 零钱兑换 II

List = list

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]


s = Solution()
print(s.change(5, [1, 2, 5]))