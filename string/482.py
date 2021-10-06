# 482. 密钥格式化

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key = [c.upper() for c in s if c != '-']
        res = []
        n = len(key)
        l = 0
        while n:
            cur_k = k
            n -= cur_k
            while n % k:
                n += 1
                cur_k -= 1
            res += key[l: l + cur_k]
            res.append("-")
            l += cur_k

        return ''.join(res[:-1])

s = Solution()
print(s.licenseKeyFormatting(s = "a0001afds-", k = 4))