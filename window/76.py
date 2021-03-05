# 76. 最小覆盖子串

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        neet = {}
        for _ in t:
            if neet.get(_):
                neet[_] = neet[_] + 1
            else:
                neet[_] = 1
        left, right, valid, start = 0, 0, 0, 0
        reslen = len(s) + 1

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            if window[c] == neet.get(c):
                valid += 1

            while valid == len(neet):
                if right - left < reslen:
                    start = left
                    reslen = right - left
                d = s[left]
                left += 1
                if neet.get(d):
                    if window[d] == neet[d]:
                        valid -= 1
                    window[d] = window[d] - 1

        return s[start:start + reslen] if reslen != len(s) + 1 else ""

s = Solution()
print(s.minWindow("a", "aa"))