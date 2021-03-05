# 56. 合并区间

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda k: k[0])
        print(intervals)
        res = [[intervals[0][0], intervals[0][1]]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append([interval[0], interval[1]])
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

s = Solution()
print(s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))