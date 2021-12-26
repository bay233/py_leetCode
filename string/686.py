# 686. 重复叠加字符串匹配


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        sb = ""
        res = 0
        while len(sb) < m:
            res += 1
            sb += a
        sb += a
        i = sb.find(b)
        if i == -1:
            return -1
        return res + 1 if i + m > n * res else res

s = Solution()
print(s.repeatedStringMatch(a = "abcd", b = "cdabcdab"))
