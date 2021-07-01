# 494. 目标和

class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:

    def findTargetSumWays(self, nums, target: int) -> int:
        nums_sum = sum(nums)
        if target > nums_sum or target < -nums_sum: return 0
        dp = [[0] * (nums_sum * 2 + 1) for _ in range(len(nums))]
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(-nums_sum, nums_sum + 1):
                if j - nums[i] >= -nums_sum:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] <= nums_sum + 1:
                    dp[i][j] += dp[i - 1][j + nums[i]]
        return dp[-1][target]

    def _findTargetSumWays(self, nums, target: int) -> int:

        book = {}

        def dp(i, target):
            if i >= len(nums) and target == 0: return 1
            if i >= len(nums): return 0
            if (i, target) in book: return book[(i, target)]
            res = dp(i + 1, target - nums[i]) + dp(i + 1, target + nums[i])
            book[(i, target)] = res
            return res

        return dp(0, target)


s = Solution()
print(s.findTargetSumWays(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))
