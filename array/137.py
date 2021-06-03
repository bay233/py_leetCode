# 137. 只出现一次的数字 II

class Solution:
    #  nums: List[int]
    def singleNumber(self, nums) -> int:
        noe, two = 0, 0
        for num in nums:
            noe = noe ^ num & ~two
            two = two ^ num & ~noe
        return noe

