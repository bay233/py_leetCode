# 1833. 雪糕的最大数量

class Solution:
    # def maxIceCream(self, costs: List[int], coins: int) -> int:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if coins >= cost:
                res += 1
                coins -= cost
            else:
                break
        return res

s = Solution()
print(s.maxIceCream(costs = [1,3,2,4,1], coins = 7))