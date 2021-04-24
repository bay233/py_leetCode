# 80. 删除有序数组中的重复项 II

class Solution:

    # 双指针
    def removeDuplicates2(self, nums) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


    def removeDuplicates(self, nums) -> int:
        count = 1
        tail = len(nums)
        i = 1
        while i < tail:
            if nums[i] == nums[i - 1]:
                if count == 2:
                    nums.append(nums.pop(i))
                    tail -= 1
                    continue
                else:
                    count += 1
            else:
                count = 1
            i += 1

        return tail


s = Solution()
print(s.removeDuplicates2([1, 1, 1, 2, 2, 3]))
