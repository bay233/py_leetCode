# 851. 喧闹和富有


List = list


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        w = [[0] * n for _ in range(n)]
        cin = [0] * n
        for a, b in richer:
            w[a][b] = 1
            cin[b] += 1
        d = []
        res = [0] * n
        for i in range(n):
            res[i] = i
            if cin[i] == 0:
                d.append(i)

        while d:
            t = d.pop(0)
            for u in range(n):
                if w[t][u] == 1:
                    if quiet[res[t]] < quiet[res[u]]:
                        res[u] = res[t]
                    cin[u] -= 1
                    if cin[u] == 0:
                        d.append(u)

        return res


s = Solution()
print(s.loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
