# 581. 最短无序连续子数组

class Solution:
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
    def findUnsortedSubarray(self, nums) -> int:
        i, j = 0, len(nums) - 1
        while i < j and nums[i] <= nums[i + 1]:
            i += 1
        while i < j and nums[j] >= nums[j - 1]:
            j -= 1

        tmp_min, tmp_max = nums[i], nums[j]
        for u in range(i, j + 1):
            if nums[u] < tmp_min:
                while i >= 0 and nums[u] < nums[i]:
                    i -= 1
                tmp_min = nums[i] if i >= 0 else float('-inf')
            if nums[u] > tmp_max:
                while j < len(nums) and nums[u] > nums[j]:
                    j += 1
                tmp_max = nums[j] if j < len(nums) else float('inf')

        return j - i - 1 if i != j else 0


s = Solution()
print(s.findUnsortedSubarray([1,3,2,4,5]))
