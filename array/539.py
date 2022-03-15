# 539. 最小时间差


List = list


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        book = []
        n = len(timePoints)
        for t in timePoints:
            ts = t.split(":")
            h, m = int(ts[0]), int(ts[1])
            book.append(h * 60 + m)

        book.sort()
        ans = 24 * 60
        for i in range(n - 1):
            ans = min(ans, book[i + 1] - book[i])
        ans = min(ans, (book[0] + (24 * 60) - book[-1]))
        return ans


s = Solution()
print(s.findMinDifference( ["00:00","23:59","00:00"]))
