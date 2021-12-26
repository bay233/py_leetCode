# 372. 超级次方


List = list


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337

        def qpow(a, b):
            ans = 1
            a %= mod
            while b != 0:
                if b & 1: ans = ans * a % mod
                a = a * a % mod
                b >>= 1
            return ans

        def dfs(a, b, u):
            if (u == -1): return 1
            return qpow(dfs(a, b, u - 1), 10) * qpow(a, b[u]) % mod

        return dfs(a, b, len(b) - 1)

s = Solution()
print(s.superPow(a = 2, b = [3]))