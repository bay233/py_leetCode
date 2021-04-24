# 90. 子集 II

class Solution:
    def subsetsWithDup(self, nums):

        def backtrack(nums, res, index, path):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums, res, i + 1, path + [nums[i]])

        res, path = [], []
        nums.sort()
        backtrack(nums, res, 0, path)
        return res

s = Solution()
print(s.subsetsWithDup([1,2,2]))