# 13. 罗马数字转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        book = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        book_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = 0
        while s:
            i = 0
            while i < 13:
                if s.startswith(book_num[i]):
                    res += book[book_num[i]]
                    s = s[len(book_num[i]):]
                else:
                    i += 1
        return res

s = Solution()
print(s.romanToInt("MCMXCIV"))
