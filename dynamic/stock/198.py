# 198. 打家劫舍

class Solution:
    def rob(self, nums: list[int]) -> int:
        a, b = 0, 0
        for num in nums:
            tmp = b
            b = max(b, a + num)
            a = tmp

        return b

s = Solution()
print(s.rob([2,7,9,3,1]))