# 517. 超级洗衣机


List = list

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        machines_sum = sum(machines)
        n = len(machines)
        if machines_sum % n:
            return -1
        avg = machines_sum // n
        res = 0
        ls, rs = 0, machines_sum
        for i in range(n):
            rs -= machines[i]
            a = max(0, i * avg - ls)
            b = max(0, (n - i - 1) * avg - rs)
            res = max(a + b, res)
            ls += machines[i]
        return res

s = Solution()
print(s.findMinMoves([0,0,11,5]))
