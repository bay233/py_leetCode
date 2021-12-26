# 1610. 可见点的最大数目
import math

List = list


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        t = angle * math.pi / 180
        book = []
        ans = 0
        for p in points:
            a = p[0] - location[0]
            b = p[1] - location[1]
            if a == 0 and b == 0:
                ans += 1
                continue
            book.append(math.atan2(a, b) + math.pi)
        book.sort()
        for i in range(len(book)):
            book.append(book[i] + 2 * math.pi)
        l, r = 0, 0
        res = 0
        while r < len(book):
            if book[r] - book[l] <= t:
                res = max(res, r - l + 1)
            else:
                while l <= r and book[r] - book[l] > t:
                    l += 1
            r += 1

        return res + ans


s = Solution()
print(s.visiblePoints([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]],0,[1,1]))
