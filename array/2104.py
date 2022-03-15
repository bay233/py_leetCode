# 2104. 子数组范围和

List = list

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            min_val, max_val = nums[i], nums[i]
            for j in range(i + 1, n):
                min_val, max_val = min(min_val, nums[j]), max(max_val, nums[j])
                ans += max_val - min_val
        return ans
