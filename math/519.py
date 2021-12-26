# 519. 随机翻转矩阵

import random

List = list


class Solution:

    def __init__(self, m: int, n: int):
        self.book = {}
        self.cnt = m * n
        self.m = m
        self.n = n

    def flip(self) -> List[int]:
        x = random.randint(0, self.cnt - 1)
        self.cnt -= 1
        idx = self.book.get(x, x)
        self.book[x] = self.book.get(self.cnt, self.cnt)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.cnt = self.m * self.n
        self.book.clear()
