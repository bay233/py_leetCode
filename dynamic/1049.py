# 1049. 最后一块石头的重量 II

class Solution:
    # def lastStoneWeightII(self, stones: List[int]) -> int:
    def lastStoneWeightII(self, stones) -> int:
        stones_sum = sum(stones)
        k = stones_sum // 2
        dp = [[0] * (k + 1) for _ in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1):
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if j >= stones[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
        return abs(stones_sum - 2 * dp[-1][-1])

s = Solution()
print(s.lastStoneWeightII(stones = [2,7,4,1,8,1]))