# 53. 最大子序和

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            if res < dp[i]: res = dp[i]

        return res


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))