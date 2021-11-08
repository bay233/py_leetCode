# 434. 字符串中的单词数

class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        space = 1
        for c in s:
            if c == ' ':
                space = 1
                continue
            if space:
                space = 0
                res += 1
        return res


s = Solution()
print(s.countSegments("  Hello,   my   name is   John  "))
