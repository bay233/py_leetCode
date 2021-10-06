# 212. 单词搜索 II

List = list


class Node:
    def __init__(self):
        self.next = [None] * 26


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()
        n = len(board)
        m = len(board[0])
        book = [[0] * m for _ in range(n)]
        offset = ord("a")
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def create(i, j, head, deept):
            if deept > 10:
                return
            for step in steps:
                if 0 <= (i + step[0]) < n and 0 <= (j + step[1]) < m:
                    x = i + step[0]
                    y = j + step[1]
                    if not book[x][y]:
                        c = board[x][y]
                        idx = ord(c) - offset
                        if not head.next[idx]:
                            head.next[idx] = Node()
                        book[x][y] = 1
                        create(x, y, head.next[idx], deept + 1)
                        book[x][y] = 0

        for i in range(n):
            for j in range(m):
                idx = ord(board[i][j]) - offset
                if not head.next[idx]:
                    head.next[idx] = Node()
                book[i][j] = 1
                create(i, j, head.next[idx], 1)
                book[i][j] = 0

        res = []
        for word in words:
            flag = True
            tmp = head
            for w in word:
                idx = ord(w) - offset
                if not tmp.next[idx]:
                    flag = False
                    break
                tmp = tmp.next[idx]
            if flag:
                res.append(word)
        return res


s = Solution()
print(s.findWords(board=[["a","b","c"],["a","e","d"],["a","f","g"]],
                  words=["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]))
