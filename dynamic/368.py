# 368. 最大整除子集

class Solution:
    # nums:List[int]
    def largestDivisibleSubset(self, nums):
        book = {}
        def dp(nums, i, tmp):
            if i == len(nums): return []
            if (tmp, i) in book: return book[(tmp, i)]
            res1 = []
            if tmp == -1 or nums[i] % tmp == 0 or tmp % nums[i] == 0:
                res1 = [nums[i]] + dp(nums, i + 1, nums[i])
            res2 = dp(nums, i + 1, tmp)
            res = res1 if len(res1) > len(res2) else res2
            book[(tmp, i)] = res
            return res
        nums.sort()
        return dp(nums, 0, -1)

s = Solution()
print(s.largestDivisibleSubset([3,4,16,8]))