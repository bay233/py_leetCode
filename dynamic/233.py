# 233. 数字 1 的个数

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        m = len(s)
        if m == 1: return 1 if n > 0 else 0
        ps = [0] * m
        ss = [0] * m
        ss[0] = int(s[1:])
        for i in range(1, m - 1):
            ps[i] = int(s[0:i])
            ss[i] = int(s[i + 1:])
        ps[-1] = int(s[:m - 1])
        res = 0
        for i in range(m):
            x = int(s[i])
            s_len = m - i - 1
            prefix = ps[i]
            suffix = ss[i]
            tot = 0
            tot += prefix * pow(10, s_len)
            if x == 1:
                tot += suffix + 1
            elif x > 1:
                tot += pow(10, s_len)
            res += tot

        return res

s = Solution()
print(s.countDigitOne(13))