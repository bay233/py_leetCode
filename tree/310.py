# 310. 最小高度树


List = list


class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        N, M, self.idx = n + 1, (n + 1) * 2, 0
        he, e, ne = [-1] * N, [0] * M, [0] * M,
        f1, f2, g, p = [0] * N, [0] * N, [0] * N, [0] * N

        def add(a, b):
            e[self.idx] = b
            ne[self.idx] = he[a]
            he[a] = self.idx
            self.idx += 1

        def dfs1(u, fa):
            i1 = he[u]
            while i1 != -1:
                j = e[i1]
                if j != fa:
                    sub = dfs1(j, u) + 1
                    if sub > f1[u]:
                        f2[u] = f1[u]
                        f1[u] = sub
                        p[u] = j
                    elif sub > f2[u]:
                        f2[u] = sub
                i1 = ne[i1]
            return f1[u]

        def dfs2(u, fa):
            i2 = he[u]
            while i2 != -1:
                j = e[i2]
                if j != fa:
                    if p[u] != j:
                        g[j] = max(g[j], f1[u] + 1)
                    else:
                        g[j] = max(g[j], f2[u] + 1)
                    g[j] = max(g[j], g[u] + 1)
                    dfs2(j, u)
                i2 = ne[i2]
        for ed in edges:
            a, b = ed[0], ed[1]
            add(a, b)
            add(b, a)
        dfs1(0, -1)
        dfs2(0, -1)
        ans = []
        min_v = n
        for i in range(n):
            cur = max(f1[i], g[i])
            if cur < min_v:
                min_v = cur
                ans.clear()
                ans.append(i)
            elif cur == min_v:
                ans.append(i)
        return ans


s = Solution()
print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))

