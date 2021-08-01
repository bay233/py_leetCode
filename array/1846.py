# 1846. 减小和重新排列数组后的最大元素

class Solution:
    # def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    def maximumElementAfterDecrementingAndRearranging(self, arr) -> int:
        sort_arr = sorted(arr)
        if sort_arr[0] != 1:
            sort_arr[0] = 1
        for i in range(1, len(sort_arr)):
            if abs(sort_arr[i] - sort_arr[i - 1]) > 1:
                sort_arr[i] -= sort_arr[i] - sort_arr[i - 1] - 1
        return sort_arr[-1]
s = Solution()
print(s.maximumElementAfterDecrementingAndRearranging(arr = [1,2,3,4,5]))
