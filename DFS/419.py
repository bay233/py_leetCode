# 419. 甲板上的战舰


List = list


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        step = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        def dfs(i, j):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return
            if board[i][j] == ".":
                return

            board[i][j] = "."
            for s in step:
                dfs(i + s[0], j + s[1])

        res = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    res += 1
                    dfs(i, j)
        return res


s = Solution()
print(s.countBattleships([["."]]))
