# 1288. 删除被覆盖区间

import functools

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        def cmp(k1, k2):
            if k1[0] != k2[0]:
                return k1[0] - k2[0]
            else:
                return k2[1] - k1[1]

        intervals.sort(key=functools.cmp_to_key(cmp))
        start = intervals[0][0]
        end = intervals[0][1]
        reslen = len(intervals)
        for interval in intervals[1:]:
            if start <= interval[0] and end >= interval[1]:
                reslen -= 1
            else:
                start = interval[0]
                end = interval[1]
        return reslen

s = Solution()
print(s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
