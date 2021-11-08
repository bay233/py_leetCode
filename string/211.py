# 211. 添加与搜索单词 - 数据结构设计

class Node:

    def __init__(self, c, end=False):
        self.c = c
        self.end = end
        self.next = {}


class WordDictionary:

    def __init__(self):
        self.root = Node('.')

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.next:
                node = node.next[c]
                continue
            else:
                node.next[c] = Node(c)
                node = node.next[c]
        node.end = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dp(i, cs):
            if i == n:
                for c, node in cs:
                    if node.end:
                        return True
                return False
            res = False
            for c, node in cs:
                w = word[i + 1] if i + 1 < n else ' '
                if c == '.':
                    res = res or dp(i + 1, [(w, node.next[a]) for a in node.next.keys()])
                elif word[i] in node.next:
                    res = res or dp(i + 1, [(w, node.next[word[i]])])
                elif '.' in node.next:
                    res = res or dp(i + 1, [(w, node.next['.'])])
            return res

        return dp(0, [(word[0], self.root)])


s = WordDictionary()
s.addWord("at")
s.addWord("and")
s.addWord("an")
s.addWord("add")
s.addWord("bat")
print(s.search(".i."))
