# 453. 最小操作次数使数组元素相等


List = list


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        min_val = min(nums)
        sum_val = sum(nums)
        return sum_val - min_val * n




s = Solution()
print(s.minMoves([-10000000,1,100000000]))