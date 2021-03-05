# 26. 删除排序数组中的重复项

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        res = 1
        while slow <= fast < len(nums) - 1:
            if nums[fast + 1] != nums[fast]:
                nums[slow+1] = nums[fast+1]
                slow += 1
                res += 1
            fast += 1
        return res

s = Solution()
print(s.removeDuplicates([1, 1, 2]))