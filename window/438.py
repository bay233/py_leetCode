# 438. 找到字符串中所有字母异位词

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window = dict()
        neet = {}
        for _ in p:
            if neet.get(_):
                neet[_] = neet[_] + 1
            else:
                neet[_] = 1
        left, right, valid = 0, 0, 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            if neet.get(c):
                if window[c] == neet.get(c):
                    valid += 1

            while right - left >= len(p):
                if valid == len(neet):
                    res.append(left)
                d = s[left]
                left += 1
                if neet.get(d):
                    if window[d] == neet[d]:
                        valid -= 1
                    window[d] = window[d] - 1
        return res


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))