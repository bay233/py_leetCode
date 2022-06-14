# 433. 最小基因变化


List = list


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        n = len(bank)
        book = [1] * n
        q = [[start]]

        def dif(a, b):
            k = len(a)
            c = 0
            for i in range(k):
                if a[i] == b[i]:
                    continue
                c += 1
            return c <= 1

        step = 1
        while q:
            level = q.pop(0)
            tmp = []
            while level:
                node = level.pop(0)
                if dif(node, end):
                    return step
                for i in range(n):
                    if book[i] and dif(node, bank[i]):
                        tmp.append(bank[i])
                        book[i] = 0
            step += 1
            if tmp:
                q.append(tmp)
        return -1


s = Solution()
print(s.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = []))
