# 2055. 蜡烛之间的盘子


List = list


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        l, r = [0] * n, [0] * n
        p, q = -1, -1
        i, j = 0, n - 1
        sum_v = [0] * (n + 1)
        while i < n:
            if s[i] == '|':
                p = i
            if s[j] == '|':
                q = j
            l[i], r[j] = p, q
            sum_v[i + 1] = sum_v[i] + (1 if s[i] == '*' else 0)
            i += 1
            j -= 1

        ans = []
        for querie in queries:
            a, b = querie[0], querie[1]
            c, d = r[a], l[b]
            if c != -1 and c <= d:
                ans.append(sum_v[d + 1] - sum_v[c])
            else:
                ans.append(0)
        return ans


s = Solution()
print(s.platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]]))
