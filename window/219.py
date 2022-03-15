# 219. 存在重复元素 II


List = list

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        n = len(nums)
        book = set()
        while r < n:
            if r - l > k:
                book.remove(nums[l])
                l += 1
            if nums[r] in book:
                return True
            book.add(nums[r])
            r += 1
        return False

s = Solution()
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))