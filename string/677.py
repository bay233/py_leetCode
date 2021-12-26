# 677. 键值映射

class Node:

    def __init__(self, val):
        self.next = {}
        self.count = val


class MapSum:

    def __init__(self):
        self.root = Node(0)

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            book = node.next
            if c not in book:
                book[c] = Node(0)
            node = node.next[c]
        node.count = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            book = node.next
            if c not in book:
                return 0
            node = node.next[c]
        return self.do_sum(node)

    def do_sum(self, node):
        if not node:
            return 0
        res = node.count
        book = node.next
        if book:
            for n in book.values():
                res += self.do_sum(n)
        return res


mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))
mapSum.insert("app", 2)
print(mapSum.sum("ap"))