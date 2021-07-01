# 773. 滑动谜题

class Solution:
    # def slidingPuzzle(self, board: List[List[int]]) -> int:
    def slidingPuzzle(self, board) -> int:
        # 空白右块向左 左块向右 下块先上 上块向下
        steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        space = [0, 0]
        for row in range(2):
            for col in range(3):
                if board[row][col] == 0:
                    space = [row, col]
                    break

        def gethash(board):
            hash_val = 0
            for row in range(2):
                for col in range(3):
                    hash_val *= 10
                    hash_val += board[row][col]
            return hash_val

        book = set()
        queue = [[board, space, 0]]
        while queue:
            stat = queue.pop(0)
            stat_map = stat[0]
            stat_space = stat[1]
            hash_val = gethash(stat_map)
            if hash_val == 123450: return stat[2]
            if hash_val not in book:
                book.add(hash_val)
                for step in steps:
                    row = stat_space[0] + step[0]
                    col = stat_space[1] + step[1]
                    if row < 0 or row > 1 or col < 0 or col > 2: continue
                    new_stat_map = []
                    new_stat_map.append(stat_map[0].copy())
                    new_stat_map.append(stat_map[1].copy())
                    new_stat_map[stat_space[0]][stat_space[1]], new_stat_map[row][col] = stat_map[row][col], 0
                    queue.append([new_stat_map, [row, col], stat[2] + 1])
        return -1

s = Solution()
print(s.slidingPuzzle([[1,2,3],[5,4,0]]))
