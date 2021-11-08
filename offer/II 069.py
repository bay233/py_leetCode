# 剑指 Offer II 069. 山峰数组的顶部


List = list

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            if arr[l + 1] < arr[l]:
                return l
            l += 1
            if arr[r - 1] < arr[r]:
                return r
            r -= 1
        return 0

s = Solution()
print(s.peakIndexInMountainArray([1,3,5,4,2]))