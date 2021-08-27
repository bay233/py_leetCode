# 413. 等差数列划分

class Solution:
    # def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    def numberOfArithmeticSlices(self, nums) -> int:
        nums_len = len(nums)
        res = 0
        i = 0
        while i < nums_len - 2:
            j = i
            d = nums[i + 1] - nums[i]
            while j + 1 < nums_len and nums[j + 1] - nums[j] == d:
                j += 1
            l = j - i + 1
            al = 1
            an = l - 3 + 1
            cnt = (al + an) * an // 2
            res += cnt
            if i == j: i += 1
            else: i = j
        return res


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
