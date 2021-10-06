# 166. 分数到小数

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        book = {}
        symbol = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            symbol = "-"
        numerator, denominator = abs(numerator), abs(denominator)
        integer = symbol + str(numerator // denominator)
        decimal = ""
        dec = numerator % denominator
        while dec:
            c = str((dec * 10) // denominator)
            decimal += c
            for k, v in book.items():
                book[k] += c
            book[dec] = c
            dec = (dec * 10) % denominator
            if dec in book:
                return integer + "." + decimal[:-len(book[dec])] + "(" + book[dec] + ")"

        if decimal != "":
            return integer + "." + decimal
        else:
            return integer

s = Solution()
print(s.fractionToDecimal(numerator = 1, denominator = 6))