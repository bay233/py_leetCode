# 600. 不含连续1的非负整数

class Solution:
    def findIntegers(self, n: int) -> int:
        bin_len = 0
        tmp = n
        while tmp:
            tmp >>= 1
            bin_len += 1

        f = [[0] * 2 for _ in range(bin_len + 1)]
        f[0][0], f[0][1] = 1, 2
        for i in range(0, bin_len):
            f[i + 1][0] = f[i][1]
            f[i + 1][1] = f[i][0] + f[i][1]

        res, pre = 0, 0
        for i in range(bin_len, -1, -1):
            cur = (n >> i) & 1
            if cur == 1:
                res += f[i][0]
            if cur == 1 and pre == 1:
                break
            pre = cur
            if i == 0:
                res += 1
        return res

s = Solution()
print(s.findIntegers(5))