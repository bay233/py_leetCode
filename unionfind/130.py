# 130. 被围绕的区域

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        leni = len(board)
        lenj = len(board[0]) if leni else 0

        def do(query):
            steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            index = len(query) - 1
            while index < len(query):
                spot = query[index]
                for step in steps:
                    x = spot[0] + step[0]
                    y = spot[1] + step[1]
                    if x < 0 or x >= leni or y < 0 or y >= lenj:
                        continue

                    if board[x][y] == "O" and [x, y] not in query:
                        query.append([x, y])
                index += 1

        query = []
        for j in range(lenj):
            for i in [0, leni - 1]:
                if board[i][j] == "O" and [i, j] not in query:
                    query.append([i, j])
                    do(query)

        for i in range(1, leni - 1):
            for j in [0, lenj - 1]:
                if board[i][j] == "O" and [i, j] not in query:
                    query.append([i, j])
                    do(query)

        for i in range(1, leni - 1):
            for j in range(1, lenj - 1):
                if board[i][j] == "O" and [i, j] not in query:
                    board[i][j] = "X"

s = Solution()
s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])