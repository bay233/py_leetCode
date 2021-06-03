# 525. 连续数组

class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    def findMaxLength(self, nums) -> int:
        book = {}
        sum_val = [0]
        for i in range(len(nums)):
            sum_val.append(sum_val[-1] + nums[i])
        res = 0
        for i in range(2, len(nums) + 1):
            key = sum_val[i - 2] * 2 - (i - 2)
            if key not in book:
                book[key] = i - 2
            if sum_val[i] * 2 - i in book:
                res = max(res, i - book[sum_val[i] * 2 - i])
        return res

s = Solution()
print(s.findMaxLength(nums = [0,1,0,1,0,0,1,1]))