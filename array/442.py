# 442. 数组中重复的数据


List = list


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            t = nums[i]
            if t < 0 or t - 1 == i:
                i += 1
                continue
            if nums[t - 1] == t:
                ans.append(t)
                nums[i] *= -1
            else:
                nums[t - 1], nums[i] = nums[i], nums[t - 1]
                i -= 1
            i += 1
        return ans


s = Solution()
print(s.findDuplicates([5,4,6,7,9,3,10,9,5,6]))
