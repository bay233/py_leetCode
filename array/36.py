# 36. 有效的数独

List = list


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        seq = [set() for _ in range(9)]
        seq_idx = 0
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                for n in range(i, i + 3):
                    for m in range(j, j + 3):
                        val = board[n][m]
                        if val == ".":
                            continue
                        if val in row[n]:
                            return False
                        else:
                            row[n].add(val)
                        if val in col[m]:
                            return False
                        else:
                            col[m].add(val)
                        if val in seq[seq_idx]:
                            return False
                        else:
                            seq[seq_idx].add(val)
                seq_idx += 1
        return True


s = Solution()
print(s.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                       [".", ".", ".", "5", "6", ".", ".", ".", "."],
                       ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                       [".", ".", ".", "7", ".", ".", ".", ".", "."],
                       [".", ".", ".", "5", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
