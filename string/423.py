# 423. 从英文中重建数字

class Solution:
    def originalDigits(self, s: str) -> str:
        res = [0] * 10
        book = {}
        for c in s:
            if c in book:
                book[c] += 1
            else:
                book[c] = 1

        def do(c, i, s):
            if c in book and book[c] > 0:
                n = book[c]
                res[i] = n
                for ch in s:
                    book[ch] -= n

        do('z', 0, 'zero')
        do('g', 8, 'eight')
        do('w', 2, 'two')
        do('h', 3, 'three')
        do('u', 4, 'four')
        do('o', 1, 'one')
        do('f', 5, 'five')
        do('v', 7, 'seven')
        do('s', 6, 'six')
        do('i', 9, 'nine')
        res_s = ""
        for i in range(10):
            if res[i]:
                res_s += str(i) * res[i]
        return res_s


s = Solution()
print(s.originalDigits("fviefuro"))
