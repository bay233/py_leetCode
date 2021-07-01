# 279. 完全平方数

class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, 100):
            val = i * i
            if val <= n:
                nums.append(val)

        nums_len = len(nums)
        dp = []
        for i in range(n + 1):
            dp.append(i)

        for i in range(1, nums_len):
            for j in range(1, n + 1):
                if j >= nums[i]:
                    dp[j] = min(dp[j], dp[j - nums[i]] + 1)
        return dp[-1]

s = Solution()
print(s.numSquares(n = 8888))