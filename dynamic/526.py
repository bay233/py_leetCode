# 526. 优美的排列

class Solution:
    def countArrangement(self, n: int) -> int:

        def getCnt(x):
            ans = 0
            while x:
                x -= (x & -x)
                ans += 1
            return ans

        mask = 1 << n
        book = [0] * mask
        book[0] = 1
        for state in range(1, mask):
            cnt = getCnt(state)
            for i in range(n):
                if not ((state >> i) & 1):
                    continue
                if (i + 1) % cnt and cnt % (i + 1):
                    continue
                book[state] += book[state & (~(1 << i))]
        return book[-1]


s = Solution()
print(s.countArrangement(2))
