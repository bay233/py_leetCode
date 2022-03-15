# 2100. 适合打劫银行的日子

List = list


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        g = [0] * n
        for i in range(1, n):
            if security[i] == security[i - 1]:
                continue
            g[i] = 1 if security[i] > security[i - 1] else -1

        a, b = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = a[i - 1] + (1 if g[i - 1] == 1 else 0)
        for i in range(1, n + 1):
            b[i] = b[i - 1] + (1 if g[i - 1] == -1 else 0)

        ans = []
        for i in range(time, n - time):
            c1 = a[i + 1] - a[i + 1 - time]
            c2 = b[i + 1 + time] - b[i + 1]
            if c1 == 0 and c2 == 0:
                ans.append(i)
        return ans
