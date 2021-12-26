# 1005. K 次取反后最大化的数组和


List = list

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                break
            i += 1
        if k == 0:
            return sum(nums)
        else:
            min_val = min(nums)
            if min_val == 0:
                return sum(nums)
            elif k & 1 == 1:
                return sum(nums) - 2 * min_val
            else:
                return sum(nums)

s = Solution()
print(s.largestSumAfterKNegations(nums = [-8,3,-5,-3,-5,-2], k = 6))
