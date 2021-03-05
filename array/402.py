# 402. 移掉K位数字

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        strlen = len(num)
        if strlen <= k: return "0"
        reslen = strlen - k
        res = []
        for i in num:
            while k and res and res[-1] > i:
                res.pop()
                k -= 1
            res.append(i)

        return str(int("".join(res[:reslen])))


s = Solution()
print(s.removeKdigits("5337", 2))