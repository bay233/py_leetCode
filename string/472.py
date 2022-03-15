# 472. 连接词
import json

List = list

class Node:

    def __init__(self, flag=False):
        self.flag = flag
        self.next = {}

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            if word == '':
                continue
            node = root
            for c in word:
                if c not in node.next:
                    node.next[c] = Node()
                node = node.next[c]
            node.flag = True


        book = {}
        def dfs(node, word, i, count):
            key = (word, i, node)
            if key in book:
                return book[key]
            if i == len(word):
                return node.flag and count > 0
            if word[i] not in node.next:
                return False
            ans = False
            next_node = node.next[word[i]]
            ans = ans or dfs(next_node, word, i + 1, count)
            if next_node.flag and not ans:
                ans = ans or dfs(root, word, i + 1, count + 1)
            book[key] = ans
            return ans

        ans = []
        for word in words:
            if dfs(root, word, 0, 0):
                ans.append(word)

        return ans

s = Solution()
with open("D:\\PyCharm\\leetcode\\input", 'r') as f:
    data = f.readline()

data = json.loads(data)
print(s.findAllConcatenatedWordsInADict(data))

