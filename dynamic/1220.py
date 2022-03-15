# 1220. 统计元音字母序列的数目


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9 + 7)
        book = [[0] * 5 for _ in range(n)]
        # 'a', 'e', 'i', 'o', 'u'
        book[0] = [1] * 5

        for i in range(n - 1):
            # 每个元音 'a' 后面都只能跟着 'e'
            book[i + 1][1] += book[i][0]
            # 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
            book[i + 1][0] += book[i][1]
            book[i + 1][2] += book[i][1]
            # 每个元音 'i' 后面 不能 再跟着另一个 'i'
            book[i + 1][0] += book[i][2]
            book[i + 1][1] += book[i][2]
            book[i + 1][3] += book[i][2]
            book[i + 1][4] += book[i][2]
            # 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
            book[i + 1][2] += book[i][3]
            book[i + 1][4] += book[i][3]
            #  每个元音 'u' 后面只能跟着 'a'
            book[i + 1][0] += book[i][4]
            for j in range(5):
                book[i + 1][j] %= MOD
        ans = 0
        for j in range(5):
            ans += book[n - 1][j]
        return ans % MOD

s = Solution()
print(s.countVowelPermutation(1))
