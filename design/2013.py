# 2013. 检测正方形


List = list


class DetectSquares:

    def __init__(self):
        self.row_col = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        col_cnt = self.row_col.get(x, {})
        col_cnt[y] = col_cnt.get(y, 0) + 1
        self.row_col[x] = col_cnt

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        ans = 0
        col_cnt = self.row_col.get(x, {})
        for ny in col_cnt.keys():
            if ny == y:
                continue
            c1 = col_cnt.get(ny)
            l = y - ny
            nums = [x + l, x - l]
            for nx in nums:
                temp = self.row_col.get(nx, {})
                c2, c3 = temp.get(y, 0), temp.get(ny, 0)
                ans += c1 * c2 * c3
        return ans
