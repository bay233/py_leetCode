# 933. 最近的请求次数


class RecentCounter:

    def __init__(self):
        self.book = []
        self.r, self.l = 0, 0

    def ping(self, t: int) -> int:
        self.book.append(t)
        self.l += 1
        while t - self.book[self.r] > 3000:
            self.r += 1
        return self.l - self.r


s = RecentCounter()
print(s.ping(1))
print(s.ping(100))
print(s.ping(3001))
print(s.ping(3002))
