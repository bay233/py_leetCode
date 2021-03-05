# 416. 分割等和子集

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s = s // 2
        dp = [[False] * (s + 1) for _ in range(len(nums))]
        for _ in range(len(nums)):
            dp[_][0] = True

        for i in range(len(nums)):
            for j in range(s + 1):
                print(i, " ", j)
                if j - nums[i] > 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                elif j == nums[i]:
                    dp[i][j] = True
                print(dp)

        return dp[len(nums)-1][s]


s = Solution()
print(s.canPartition([1, 5, 11, 5]))