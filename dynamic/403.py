# 403. 青蛙过河

class Solution:
    # stones: List[int]
    def canCross(self, stones) -> bool:
        book = {}
        set_stones = set(stones)
        def dp(stones, pos, k):
            if pos not in set_stones: return False
            if pos == stones[-1]: return True
            if (pos, k) in book: return book[(pos, k)]

            res1, res2 = False, False
            if k - 1 > 0:
                res1 = dp(stones, pos + (k - 1), k - 1)
            if k > 0:
                res2 = dp(stones, pos + k, k)
            res3 = dp(stones, pos + k + 1, k + 1)
            res = res1 or res2 or res3
            book[(pos, k)] = res
            return res

        return dp(stones, 0, 0)


s = Solution()
print(s.canCross([0,1,3,5,6,8,12,17]))
