# 171. Excel 表列序号

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for s in columnTitle:
            res = res * 26 + ord(s) - 64
        return res

    def numberToTitle(self, number: int) -> str:
        if number <= 26: return chr(64 + number)
        return self.numberToTitle(number // 26) + chr(64 + (number % 26))


s = Solution()
print(s.titleToNumber("ZY"))
print(s.numberToTitle(2147483647))