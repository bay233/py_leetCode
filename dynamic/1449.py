# 1449. 数位成本和为目标值的最大数字

class Solution:
    # def largestNumber(self, cost: List[int], target: int) -> str:
    def largestNumber(self, cost, target: int) -> str:
        cost_book = {}
        for i in range(len(cost)):
            val = cost[i]
            if val in cost_book:
                cost_book[val] = max(cost_book[val], i + 1)
            else:
                cost_book[val] = i + 1

        def dp_sum(dd):
            v = 0
            for d in dd:
                v = v * 10 + d
            return v

        def dp_max(d1, d2):
            d1.sort(reverse=True)
            d2.sort(reverse=True)
            return d1 if dp_sum(d1) > dp_sum(d2) else d2

        dp = [[]] * (target + 1)
        for i in range(1, target + 1):
            for k, v in cost_book.items():
                if i == k:
                    dp[i] = dp_max(dp[i], [v])
                elif i >= k and dp[i - k]:
                    tmp = dp[i - k].copy()
                    tmp.append(v)
                    dp[i] = dp_max(dp[i], tmp)
        return str(dp_sum(dp[-1]))


s = Solution()
print(s.largestNumber(cost = [6,10,15,40,40,40,40,40,40], target = 47))
