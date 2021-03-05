# 435. 无重叠区间

List = list
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        tail = float("-inf")
        res = 0
        for interval in intervals:
            head = interval[0]
            if tail < head:
                tail = interval[-1]
                res += 1
        return res


s = Solution()
print(s.eraseOverlapIntervals([[2,3],[2,3]]))