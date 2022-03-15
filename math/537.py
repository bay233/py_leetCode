# 537. 复数乘法


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num_str = num1.split('+')
        a1, b1 = int(num_str[0]), int(num_str[1][:-1])
        num_str = num2.split('+')
        a2, b2 = int(num_str[0]), int(num_str[1][:-1])
        a = a1 * a2 - b1 * b2
        b = a1 * b2 + a2 * b1
        ans = '0' if a == 0 else str(a)
        ans += '+'
        ans += '0' if b == 0 else str(b)
        ans += 'i'
        return ans


s = Solution()
print(s.complexNumberMultiply(num1 = "1+-1i", num2 = "1+-1i"))
