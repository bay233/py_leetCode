# 821. 字符的最短距离


List = list


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = s.index(c)
        r = l
        n = len(s)
        ans = []
        for i in range(n):
            if i > r != -1:
                l = r
                if r + 1 < n:
                    r = s.find(c, r + 1)
            ans.append(min(abs(l - i), abs(i - r)))
        return ans


s = Solution()
print(s.shortestToChar(s = "bbaa", c = "b"))
