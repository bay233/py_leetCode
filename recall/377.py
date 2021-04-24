# 377. 组合总和 Ⅳ

class Solution:
    # nums:List[int]
    def combinationSum4(self, nums, target: int) -> int:
        book = {}

        def dp(nums, target, sum_val, depth):
            if sum_val == target:
                return 1
            if sum_val > target:
                return 0
            if (depth, sum_val) in book: return book[(depth, sum_val)]
            res = 0
            for i in range(len(nums)):
                res += dp(nums, target, sum_val + nums[i], depth + 1)
            book[(depth, sum_val)] = res
            return res

        return dp(nums, target, 0, 0)

        # nums:List[int]

    def combinationSum4_2(self, nums, target: int) -> int:
        if not nums: return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


s = Solution()
print(s.combinationSum4_2([4, 2, 1], 32))
