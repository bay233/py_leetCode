# 794. 有效的井字游戏


List = list


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        cs = [[''] * 3 for i in range(3)]
        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                c = board[i][j]
                if c == 'X':
                    x += 1
                if c == 'O':
                    o += 1
                cs[i][j] = c

        def check(cs, c):
            for i in range(3):
                if cs[i][0] == c and cs[i][1] == c and cs[i][2] == c:
                    return True
                if cs[0][i] == c and cs[1][i] == c and cs[2][i] == c:
                    return True
            a, b = True, True
            for i in range(3):
                for j in range(3):
                    if i == j:
                        a &= cs[i][j] == c
                    if i + j == 2:
                        b &= cs[i][j] == c
            return a or b

        a, b = check(cs, 'X'), check(cs, 'O')
        if o > x or x - o > 1: return False
        if a and x <= o: return False
        if b and o != x: return False
        if a and b: return False
        return True

s = Solution()
print(s.validTicTacToe(["OXX","XOX","OXO"]))