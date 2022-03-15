# 1994. 好子集的数目


List = list

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = int(1e9+7)
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnts = [0] * 31
        for i in nums:
            cnts[i] += 1
        mask = 1 << 10
        f = [0] * mask
        f[0] = 1
        for i in range(2, 31):
            if cnts[i] == 0:
                continue
            cur, x = 0, i
            ok = True
            for j in range(10):
                t, c = p[j], 0
                while x % t == 0:
                    cur |= (1 << j)
                    x //= t
                    c += 1
                if c > 1:
                    ok = False
                    break
            if not ok:
                continue
            for prev in range(mask - 1, -1, -1):
                if (prev & cur) != 0:
                    continue
                f[prev | cur] = (f[prev | cur] + f[prev] * cnts[i]) % MOD

        ans = 0
        for i in range(1, mask):
            ans = (ans + f[i]) % MOD
        for i in range(cnts[1]):
            ans = ans * 2 % MOD
        return ans

s = Solution()
print(s.numberOfGoodSubsets([1,2,3,4]))
