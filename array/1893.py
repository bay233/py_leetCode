# 1893. 检查是否区域内所有整数都被覆盖

class Solution:
    # def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        diff = [0] * 52
        for t_range in ranges:
            diff[t_range[0]] += 1
            diff[t_range[1] + 1] -= 1
        diff_sum = [0]
        for i in diff[1:]:
            diff_sum.append(diff_sum[-1] + i)
        for i in range(left, right + 1):
            if diff_sum[i] <= 0:
                return False
        return True

s = Solution()
print(s.isCovered([[1,10],[10,20]], 21, 21))