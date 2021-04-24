# 219. 存在重复元素 II

class Solution:
    # nums:List[int]
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        book = set()
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] in book: return True
            book.add(nums[fast])
            fast += 1
            if fast - slow > k:
                book.remove(nums[slow])
                slow += 1
        return False


s = Solution()
print(s.containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))
