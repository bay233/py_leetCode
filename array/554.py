# 554. 砖墙

class Solution:
    # wall: List[List[int]]
    def leastBricks(self, wall) -> int:
        book = {0: 0}
        for i in range(len(wall)):
            tmp = 0
            for j in range(len(wall[i]) - 1):
                tmp += wall[i][j]
                if tmp in book:
                    book[tmp] = book[tmp] + 1
                else:
                    book[tmp] = 1
        return len(wall) - max(book.values())


s = Solution()
print(s.leastBricks([[100000000], [100000000], [100000000]]))


