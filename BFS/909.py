# 909. 蛇梯棋

class Solution:
    # def snakesAndLadders(self, board: List[List[int]]) -> int:
    def snakesAndLadders(self, board) -> int:
        row_len = len(board)
        col_len = row_len
        end = row_len * col_len

        def get_coordinate(step):
            step -= 1
            row = step // col_len
            col = step % col_len
            direction = row & 1
            if direction:
                col = -(col + 1)
            return row_len - row - 1, col

        book = set()
        queue = [[1]]
        res = 0
        while queue:
            res += 1
            step_queues = queue.pop()
            tmp_queue = []
            while step_queues:
                step = step_queues.pop()
                for i in range(1, 7):
                    nex_step = step + i
                    if nex_step > end: break
                    row, col = get_coordinate(nex_step)
                    if board[row][col] != -1:
                        nex_step = board[row][col]
                    if nex_step == end: return res
                    if nex_step in book:
                        continue
                    book.add(nex_step)
                    tmp_queue.append(nex_step)
            if tmp_queue: queue.append(tmp_queue)
            # print(tmp_queue, " ", max(tmp_queue))
        return -1


s = Solution()
print(s.snakesAndLadders(
    [[-1, 60, 32, -1, -1, -1, 59, -1],
     [34, 1, 15, 9, 13, 25, 63, 26],
     [-1, -1, -1, -1, 29, -1, -1, -1],
     [-1, -1, -1, 27, -1, -1, -1, 5],
     [6, 59, -1, 2, 40, 13, -1, -1],
     [-1, 44, 20, -1, -1, -1, 58, -1],
     [-1, -1, 9, -1, -1, 23, -1, -1],
     [-1, -1, -1, 46, 27, 6, -1, -1]]))

print(s.snakesAndLadders(
    [[1,1,-1],[1,1,1],[-1,1,1]]))
