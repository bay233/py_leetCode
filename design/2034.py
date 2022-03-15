# 2034. 股票价格波动

from sortedcontainers import sortedlist


class StockPrice:

    def __init__(self):
        self.data = {}
        self.date = sortedlist.SortedList()
        self.val = sortedlist.SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.data:
            self.val.remove(self.data[timestamp])
        self.val.add(price)
        self.data[timestamp] = price
        self.date.add(timestamp)

    def current(self) -> int:
        return self.data[self.date[-1]]

    def maximum(self) -> int:
        return self.val[-1]

    def minimum(self) -> int:
        return self.val[0]

s = StockPrice()
s.update(1, 10)
s.update(2, 5)
print(s.current())
print(s.maximum())
s.update(1, 3)
print(s.maximum())