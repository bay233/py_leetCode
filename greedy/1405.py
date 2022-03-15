# 1405. 最长快乐字符串

from sortedcontainers import sortedlist



class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = sortedlist.SortedList(key=lambda x: -x[0])
        if a > 0:
            q.add([a, 'a'])
        if b > 0:
            q.add([b, 'b'])
        if c > 0:
            q.add([c, 'c'])

        ans = []
        while q:
            t = q.pop(0)
            if len(ans) <= 1 or ans[-1] != t[1] or ans[-2] != t[1]:
                ans.append(t[1])
                t[0] -= 1
            else:
                if not q:
                    break
                t2 = q.pop(0)
                ans.append(t2[1])
                t2[0] -= 1
                if t2[0] > 0:
                    q.add(t2)
            if t[0] > 0:
                q.add(t)

        return ''.join(ans)

s = Solution()
print(s.longestDiverseString(a = 7, b = 1, c = 0))