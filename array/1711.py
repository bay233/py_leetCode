# 1711. 大餐计数

class Solution:
    # def countPairs(self, deliciousness: List[int]) -> int:
    def countPairs(self, deliciousness) -> int:
        book = {}
        for deliciousnes in deliciousness:
            if deliciousnes in book:
                book[deliciousnes] += 1
            else:
                book[deliciousnes] = 1

        def fun(n, m):
            r1 = 1
            for _ in range(m):
                r1 *= n
                n -= 1
            r2 = 1
            tmp = 1
            for _ in range(m):
                r2 *= tmp
                tmp += 1
            return r1 // r2
        res = 0
        for k in list(book.keys()):
            tmp = 1 << 31
            while k <= tmp and tmp:
                if (tmp - k) in book:
                    if tmp - k == k:
                        res += fun(book[k], 2)
                    else:
                        res += book[k] * book[tmp - k]
                tmp >>= 1
            book.pop(k)
        return res % (10 ** 9 + 7)


s = Solution()
print(s.countPairs(
    [64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
     64, 64, 64, 64]))
print(s.countPairs([1, 1, 1, 3, 3, 3, 7]))
