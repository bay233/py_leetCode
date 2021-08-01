# 剑指 Offer 53 - I. 在排序数组中查找数字 I

class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target: int) -> int:
        def scl(val):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] >= val:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        def scr(val):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        l, r = scl(target), scr(target)
        return r - l - 1
s = Solution()
print(s.search(nums = [5,7,7,8,8,8,8,10], target = 0))
