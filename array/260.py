# 260. 只出现一次的数字 III

class Solution:
    # singleNumber(self, nums: List[int]) -> List[int]:
    def singleNumber(self, nums):
        t = 0
        for num in nums:
            t ^= num
        m = t & -t
        res1, res2 = 0, 0
        for num in nums:
            if (num & m) == m:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]


s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))