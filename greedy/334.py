# 334. 递增的三元子序列


List = list


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        low, mid = 2 << 31 - 1, 2 << 31 - 1
        for num in nums:
            if num < low:
                low = num
                mid = low
            elif num < mid:
                mid = mid
            elif num > mid:
                return True
        return False



s = Solution()
print(s.increasingTriplet([9,10,5,11,10,9,8]))
