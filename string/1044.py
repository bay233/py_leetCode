# 1044. 最长重复子串


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        def check(lenght):
            book = set()
            for i in range(0, n - lenght + 1):
                j = i + lenght
                cur = s[i: j]
                if cur in book:
                    return cur
                book.add(cur)
            return ""

        ans = ""
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            t = check(mid)
            if len(t) != 0:
                l = mid
            else:
                r = mid - 1
            ans = t if len(t) > len(ans) else ans

        return ans

s = Solution()
print(s.longestDupSubstring("aa"))