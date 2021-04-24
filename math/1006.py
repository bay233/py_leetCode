# 1006. 笨阶乘

class Solution:
    def clumsy(self, N: int) -> int:
        def judge(N):
            if N == 0: return 0
            if N == 3:
                return N * (N - 1) // (N - 2)
            if N == 2:
                return N * (N - 1)
            if N == 1:
                return N

        def run(N):
            if N < 4:
                return judge(N)
            return N * (N - 1) // (N - 2) - (N - 3) + run(N - 4)
        if N < 4:
            return judge(N)
        return N * (N - 1) // (N - 2) + (N - 3) - run(N - 4)


s = Solution()
print(s.clumsy(4))
