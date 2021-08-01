# 1877. 数组中最大数对和的最小值

class Solution:
    # def minPairSum(self, nums: List[int]) -> int:
    def minPairSum(self, nums) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = float('-inf')
        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        return res

s = Solution()
print(s.minPairSum(nums = [3,5,2,3]))