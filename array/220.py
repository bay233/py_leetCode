# 220. 存在重复元素 III

class Solution:
    # nums:List[int]
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        def getIdx(val):
            return val // (t + 1) - 1 if val < 0 else val // (t + 1)

        book = {}
        for i, val in enumerate(nums):
            idx = getIdx(val)
            # 如果目标桶已存在直接放回true
            if idx in book: return True
            # 如果不存在查找相邻的桶
            l, r = idx - 1, idx + 1
            if l in book and abs(val - book[l]) <= t:
                return True
            if r in book and abs(val - book[r]) <= t:
                return True
            # 建立桶
            book[idx] = val
            # 将下标范围外的桶清除
            if i >= k:
                book.pop(getIdx(nums[i - k]))

        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
