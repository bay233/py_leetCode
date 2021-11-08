# 38. 外观数列

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        s = self.countAndSay(n - 1) + ' '
        res = ''
        tmp_c = s[0]
        tmp_n = 0
        for c in s:
            if tmp_c != c:
                res += str(tmp_n) + tmp_c
                tmp_c = c
                tmp_n = 0
            tmp_n += 1
        return res


s = Solution()
print(s.countAndSay(30))
