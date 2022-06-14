# 462. 最少移动次数使数组元素相等 II


List = list

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        t = nums[n // 2]
        ans = 0
        for i in nums:
            ans += abs(t - i)
        return ans
