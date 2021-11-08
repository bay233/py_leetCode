# 869. 重新排序得到 2 的幂

class Node:
    def __init__(self):
        self.next = {}
        self.flag = False


class Solution:

    def __init__(self):
        self.root = Node()
        i = 1
        n = 10 ** 9
        while i <= n:
            s = list(str(i))
            s.sort(key=lambda x: int(x), reverse=True)
            node = self.root
            for c in s:
                if c not in node.next:
                    node.next[c] = Node()
                node = node.next[c]
            node.flag = True
            i <<= 1

    def reorderedPowerOf2(self, n: int) -> bool:
        s = list(str(n))
        s.sort(key=lambda x: int(x), reverse=True)
        node = self.root
        for c in s:
            if node and c in node.next:
                node = node.next[c]
            else:
                return False
        return True if node.flag else False

s = Solution()
print(s.reorderedPowerOf2(1041))
