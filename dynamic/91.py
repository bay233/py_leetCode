# 91. 解码方法

class Solution:
    def numDecodings(self, s: str) -> int:
        book = {}
        def dp(s):
            if len(s) == 0: return 1
            if int(s[0]) == 0: return 0
            if len(s) == 1: return 1
            if s in book: return book[s]
            res = 0
            if 0 < int(s[0]) <= 2:
                if int(s[1]) == 0:
                    res += dp(s[2:])
                elif int(s[0]) == 2 and int(s[1]) > 6:
                    res += dp(s[1:])
                else:
                    res += dp(s[1:])
                    if len(s) >= 2:
                        res += dp(s[2:])
            else:
                if int(s[1]) != 0:
                    res += dp(s[1:])
            book[s] = res
            return res
        return dp(s)

s = Solution()
print(s.numDecodings("27"))