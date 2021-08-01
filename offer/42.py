# 剑指 Offer 42. 连续子数组的最大和

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums) -> int:
        low, fast = 0, 0
        res_max = nums[low]
        cur_sum = nums[low]
        while fast < len(nums) - 1:
            fast += 1
            cur_sum += nums[fast]
            res_max = max(res_max, cur_sum)
            while cur_sum <= nums[fast] and low < fast:
                cur_sum -= nums[low]
                res_max = max(res_max, cur_sum)
                low += 1
        return res_max


s = Solution()
print(s.maxSubArray(nums= [-2,1,-3,4,-1,2,1,-5,4]))
