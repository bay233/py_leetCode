# 299. 猜数字游戏

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        book = {}
        n = len(secret)

        a, b = 0, 0
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                book[secret[i]] = book.get(secret[i], 0) + 1
        for i in range(n):
            if secret[i] != guess[i] and book.get(guess[i], 0) > 0:
                book[guess[i]] -= 1
                b += 1

        return str(a) + 'A' + str(b) + 'B'


s = Solution()
print(s.getHint(secret = "1", guess = "0"))
