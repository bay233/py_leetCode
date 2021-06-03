# 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？

class Solution:
    # def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    def canEat(self, candiesCount, queries):
        res = []
        sum_head = [0]
        for candies in candiesCount:
            sum_head.append(sum_head[-1] + candies)
        for querie in queries:
            lower, upper = sum_head[querie[0]], sum_head[querie[0] + 1]
            day = querie[1] + 1
            if day >= upper or (day + 1) * querie[-1] <= lower:
                res.append(False)
            else:
                res.append(True)
        return res

s = Solution()
print(s.canEat(candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]))
