# 495. 提莫攻击


List = list


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        start, end = 0, 0
        for time in timeSeries:
            if time <= end:
                end = time + duration
            else:
                res += end - start
                start, end = time, time + duration
        res += end - start
        return res


s = Solution()
print(s.findPoisonedDuration(timeSeries=[1, 2], durat6ion=2))
