# 313. 超级丑数

from sortedcontainers.sortedlist import SortedList

class Solution:
    # def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        book = set()
        q = SortedList()
        q.add(1)
        book.add(1)
        while n >= 0:
            n -= 1
            x = q.pop(0)
            if not n: return x
            for p in primes:
                t = x * p
                if t not in book:
                    book.add(t)
                    q.add(t)
        return -1

s = Solution()
print(s.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))