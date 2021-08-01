# 645. 错误的集合

class Solution:
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    def findErrorNums(self, nums):
        num_sum = 0
        num_sum_t = 0
        res = 0
        book = set()
        for i in range(len(nums)):
            if nums[i] in book:
                res = nums[i]
            else:
                book.add(nums[i])
            num_sum_t += i + 1
            num_sum += nums[i]
        return [res, num_sum_t - num_sum + res]

s = Solution()
print(s.findErrorNums(nums =[8,7,3,5,3,6,1,4]))