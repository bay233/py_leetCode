# 638. 大礼包


List = list


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)

        def check(sp, need):
            for i in range(n):
                if sp[i] > need[i]:
                    return False
            return True

        def sub(sp, need):
            res = [0] * n
            for i in range(n):
                res[i] = need[i] - sp[i]
            return res

        book = {}
        def dp(need):
            key = tuple(need)
            if key in book:
                return book[key]

            min_res = float('inf')
            for sp in special:
                if check(sp, need):
                    min_res = min(min_res, dp(sub(sp, need)) + sp[-1])
            res = 0
            for i in range(n):
                res += price[i] * need[i]
            min_res = min(min_res, res)
            book[key] = min_res
            return min_res

        return dp(needs)

s = Solution()
print(s.shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]))