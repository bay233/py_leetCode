# 1713. 得到子序列的最少操作次数

class Solution:
    # def minOperations(self, target: List[int], arr: List[int]) -> int:
    def minOperations(self, target, arr) -> int:
        n, m = len(target), len(arr)
        book = {}
        for i, t in enumerate(target):
            book[t] = i

        arr_idx = []
        for a in arr:
            if a in book:
                arr_idx.append(book[a])

        res_max = 0
        arr_idx_len = len(arr_idx)
        f = [0] * arr_idx_len
        g = [float('inf')] * (arr_idx_len + 1)

        for i in range(arr_idx_len):
            l, r = 0, i
            while l < r:
                mid = l + r + 1 >> 1
                if g[mid] < arr_idx[i]:
                    l = mid
                else:
                    r = mid - 1
            clen = r + 1
            f[i] = clen
            g[clen] = min(g[clen], arr_idx[i])
            res_max = max(res_max, clen)
        return n - res_max