# 382. 链表随机节点
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: [ListNode]):
        self.book = []
        node = head
        while node:
            self.book.append(node.val)
            node = node.next
        self.n = len(self.book)

    def getRandom(self) -> int:
        return self.book[random.randint(0, self.n - 1)]