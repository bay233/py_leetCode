# 386. 字典序排数


List = list


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dp(v):
            if v > n:
                return
            ans.append(v)
            for i in range(10):
                dp(v * 10 + i)

        for i in range(1, 10):
            dp(i)
        return ans


s = Solution()
print(s.lexicalOrder(13))
