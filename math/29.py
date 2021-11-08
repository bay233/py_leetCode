# 29. 两数相除

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        a, b = dividend, divisor
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            flag = True
        if a < 0: a = -a
        if b < 0: b = -b
        res = 0
        while a >= b:
            s, i = b, 1
            while a >= (s << 1):
                s <<= 1
                i <<= 1
            res += i
            a -= s

        res = -res if flag else res
        return res if res <= 2147483647 else 2147483647

s = Solution()
print(s.divide(-2147483648, -1))