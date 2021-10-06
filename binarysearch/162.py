# 162. 寻找峰值


List = list

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r