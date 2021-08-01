# 面试题 17.10. 主要元素

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums) -> int:
        x = -1
        count = 0
        for num in nums:
            if count == 0:
                x = num
                count = 1
            else:
                count += 1 if x == num else -1
        count = 0
        for num in nums:
            if num == x:
                count += 1
        return x if count > len(nums) // 2 else -1

s = Solution()
print(s.majorityElement([3,3,4]))