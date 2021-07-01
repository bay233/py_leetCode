# 168. Excel表列名称

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            base = columnNumber
            n = 0
            while base > 26:
                if base % 26 == 0:
                    base = base // 26 - 1
                else:
                    base = base // 26
                n += 1
            res += chr(base + 64)
            columnNumber -= base * 26 ** n
        return res

s = Solution()
print(s.convertToTitle(520))

print(ord("A"), chr(65))

