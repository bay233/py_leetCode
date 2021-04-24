# 87. 扰乱字符串

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        book = {}
        def dp (s1, s2):
            if s1 + s2 in book: return book[s1 + s2]
            if len(s1) != len(s2):
                book[s1 + s2] = False
                return False
            if s1 == s2:
                book[s1 + s2] = True
                return True
            if sorted(s1) != sorted(s2):
                book[s1 + s2] = False
                return False
            for i in range(1, len(s1)):
                if (dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:])) \
                        or (dp(s1[:i], s2[-i:]) and dp(s1[i:], s2[:-i])):
                    return True
            book[s1 + s2] = False
            return False
        return dp(s1, s2)

s = Solution()
print(s.isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))
