# 12. 整数转罗马数字

class Solution:
    def intToRoman(self, num: int) -> str:
        book = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
                4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

        book_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        if num:
            i = 0
            while i < 13:
                if num - book_num[i] >= 0:
                    res += book[book_num[i]]
                    num -= book_num[i]
                else:
                    i += 1
        return res

s = Solution()
print(s.intToRoman(1994))