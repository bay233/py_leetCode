# 34. 在排序数组中查找元素的第一个和最后一个位置

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def leftRange(nums: list[int], target: int) -> int:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if l >= len(nums) or nums[l] != target:
                return -1
            return l

        def rightRange(nums: list[int], target: int) -> int:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if r < 0 or nums[r] != target:
                return -1
            return r

        return [leftRange(nums, target), rightRange(nums, target)]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
