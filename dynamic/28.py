# 28. 实现 strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle: return 0
        if not needle: return 0
        if not haystack: return -1

        def getkmp_next(sstr):
            kmp_next = [0] * len(sstr)
            kmp_next[0] = -1
            k, j = -1, 0
            while j < len(sstr) - 1:
                if k == -1 or sstr[k] == sstr[j]:
                    k += 1
                    j += 1
                    if sstr[k] == sstr[j]:
                        kmp_next[j] = kmp_next[k]
                    else:
                        kmp_next[j] = k
                else:
                    k = kmp_next[k]
            return kmp_next

        kmp_next = getkmp_next(needle)
        h, n = len(haystack), len(needle)
        i, j = 0, 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = kmp_next[j]
            if j == n: return i - j

        return -1


s = Solution()
print(s.strStr("babbb", "ab"))
