# 306. 累加数


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def dp(a1, a2, start):
            if start >= n:
                return False
            if a1 + a2 == int(num[start: n]) and (num[start] != "0" or n - start == 1):
                return True

            res = False
            for i in range(start, n):
                if num[start] == "0" and i - start > 0:
                    break
                b = int(num[start: i + 1])
                if a1 + a2 == b:
                    res = res or dp(a2, b, i + 1)
            return res

        ans = False
        for i in range(n - 1):
            if num[0] == "0" and i > 0:
                continue
            for j in range(i + 1, n):
                if num[i + 1] == "0" and j - i > 1:
                    continue
                if ans:
                    return ans
                a1, a2 = int(num[0: i + 1]), int(num[i + 1: j + 1])
                ans = ans or dp(a1, a2, j + 1)
        return ans


s = Solution()
print(s.isAdditiveNumber("1203"))
