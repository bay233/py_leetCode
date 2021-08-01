# 1838. 最高频元素的频数

class Solution:
    # def maxFrequency(self, nums: List[int], k: int) -> int:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        l, r = 0, 0
        res = 1
        while r < len(nums):
            r += 1
            if (pre_sum[r] - pre_sum[l] + k) // (r - l) < nums[r - 1] and l < r:
                l += 1
            res = max(res, r - l)

        return res

s = Solution()
print(s.maxFrequency(nums = [1,4,8,13], k = 5))
