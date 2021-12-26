# 1705. 吃苹果的最大数目

from sortedcontainers import sortedlist

List = list

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q = sortedlist.SortedList(key= lambda x: x[1])
        n = len(apples)
        ans = 0
        for i in range(n):
            if apples[i] != 0:
                day = [apples[i], days[i] + i]
                q.add(day)
            if q:
                while q and q[0][1] <= i:
                    q.pop(0)
                if not q:
                    continue
                d = q[0]
                if d[0] == 1:
                    q.pop(0)
                else:
                    d[0] -= 1
                ans += 1
        i = n
        while q:
            d = q.pop(0)
            num = min(d[0], d[1] - i)
            if num > 0:
                ans += num
                i += num
        return ans

s = Solution()
print(s.eatenApples( [3,0,0,0,0,2], days = [3,0,0,0,0,2]))

