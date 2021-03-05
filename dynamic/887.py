# 887. 鸡蛋掉落

class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        book = dict()
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in book: return book[(K, N)]
            res = float('INF')
            l, r = 1, N
            while l <= r:
                mid = (l + r) // 2
                broken = dp(K - 1, mid - 1) # 蛋碎了
                no_broken = dp(K, N - mid) # 蛋没碎
                if broken > no_broken:
                    r = mid - 1
                    res = min(res, broken + 1)
                else:
                    l = mid + 1
                    res = min(res, no_broken + 1)

            book[(K, N)] = res
            return res
        return dp(K, N)

    def superEggDrop2(self, K: int, N: int) -> int:
        book = dict()

        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in book: return book[(K, N)]
            res = float('INF')
            for i in range(1, N + 1):
                res = min(res, max(dp(K - 1, i - 1),
                                   dp(K, N - i)) + 1)

            book[(K, N)] = res
            return res

        return dp(K, N)


s = Solution()
print(s.superEggDrop2(2, 200))
print(s.superEggDrop(2, 2000000))
