# 611. 有效三角形的个数

class Solution:
    # def triangleNumber(self, nums: List[int]) -> int:
    def triangleNumber(self, nums) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n):
            k = 0
            j = i - 1
            while j > k:
                while k < j and nums[k] + nums[j] <= nums[i]:
                    k += 1
                res += j - k
                j -= 1
        return res


s = Solution()
print(s.triangleNumber(
    [2,2,3,4]))
