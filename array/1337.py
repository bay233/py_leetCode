# 1337. 矩阵中战斗力最弱的 K 行

import functools

class Solution:
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    def kWeakestRows(self, mat, k: int):
        res = []
        for i in range(len(mat)):
            num = 0
            for val in mat[i]:
                if val == 1:
                    num += 1
                else:
                    break
            res.append((i, num))

        def key(a, b):
            if a[1] != b[1]: return a[1] - b[1]
            return a[0] - b[0]
        res.sort(key=functools.cmp_to_key(key))
        return [res[i][0] for i in range(k)]

s = Solution()
print(s.kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))
