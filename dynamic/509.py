# 509. 斐波那契数

class Solution:
    def fib(self, n: int) -> int:
        pre, suf = 0, 1
        for i in range(n):
            pre, suf = suf, pre + suf
        return pre
