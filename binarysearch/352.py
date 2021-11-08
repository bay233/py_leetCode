# 352. 将数据流变为多个不相交区间

List = list


class SummaryRanges:

    def __init__(self):
        self.book = []

    def addNum(self, val: int) -> None:
        if not self.book:
            self.book.append([val, val])
        l, r = 0, len(self.book) - 1
        while l <= r:
            mid = l + r >> 1
            a, b = self.book[mid][0], self.book[mid][1]
            if val < a:
                r = mid - 1
            elif val > b:
                l = mid + 1
            else:
                return
        idx = l
        if idx - 1 >= 0 and idx < len(self.book):
            if val - 1 == self.book[idx - 1][1] and val + 1 == self.book[idx][0]:
                tmp = [self.book[idx - 1][0], self.book[idx][1]]
                self.book[idx - 1] = tmp
                self.book.pop(idx)
            elif val - 1 == self.book[idx - 1][1]:
                tmp = [self.book[idx - 1][0], val]
                self.book[idx - 1] = tmp
            elif val + 1 == self.book[idx][0]:
                tmp = [val, self.book[idx][1]]
                self.book[idx] = tmp
            else:
                self.book.insert(idx, [val, val])
        elif idx - 1 < 0:
            if val + 1 == self.book[idx][0]:
                tmp = [val, self.book[idx][1]]
                self.book[idx] = tmp
            else:
                self.book.insert(idx, [val, val])
        else:
            if val - 1 == self.book[idx - 1][1]:
                tmp = [self.book[idx - 1][0], val]
                self.book[idx - 1] = tmp
            else:
                self.book.append([val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.book


s = SummaryRanges()
print(s.addNum(1))
print(s.addNum(3))
print(s.addNum(7))
print(s.addNum(2))
print(s.addNum(6))
