# 877. 石子游戏

List = list


class Solution:

    def stoneGame2(self, piles: List) -> bool:

        sum_pile = sum(piles)
        book = [[-1] * len(piles) for _ in range(len(piles))]
        def dp(piles, i, j):
            if i > j: return 0
            if book[i][j] != -1: return book[i][j]
            yali = max(min(dp(piles, i + 1, j - 1), dp(piles, i + 2, j)) + piles[i],
                       min(dp(piles, i, j - 2), dp(piles, i + 1, j - 1)) + piles[j])
            book[i][j] = yali
            return yali

        yali = dp(piles, 0, len(piles) - 1)
        print(yali)
        return yali > sum_pile // 2

    def stoneGame(self, piles: List) -> bool:
        sum_pile = sum(piles)

        def dp(piles):
            if not piles: return 0
            yali = max(min(dp(piles[1:-1]), dp(piles[2:])) + piles[0],
                       min(dp(piles[:-2]), dp(piles[1:-1])) + piles[-1])
            return yali

        return dp(piles) > sum_pile // 2


s = Solution()
print(s.stoneGame2([7, 7, 12, 16, 41, 48, 41]))
