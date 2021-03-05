# 213. 打家劫舍 II

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        a1, b1 = 0, 0
        a2, b2 = 0, 0
        for i in range(len(nums)):
            if i != len(nums) - 1:
                tmp1 = b1
                b1 = max(b1, a1 + nums[i])
                a1 = tmp1
            if i != 0:
                tmp2 = b2
                b2 = max(b2, a2 + nums[i])
                a2 = tmp2
        return max(b1, b2)

        # def rob(nums: list[int]) -> int:
        #     a, b = 0, 0
        #     for num in nums:
        #         tmp = b
        #         b = max(b, a + num)
        #         a = tmp
        #     return max(a, b)
        #
        # if len(nums) < 2: return 0
        # return max(rob(nums[:-1]), rob(nums[1:]))


s = Solution()
print(s.rob([1,2,3,1]))
