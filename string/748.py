# 748. 最短补全词


List = list

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        book = {}
        for c in licensePlate:
            sc = ord(c)
            if 48 <= sc < 58 or c == ' ':
                continue
            low_c = c.lower()
            if low_c in book:
                book[low_c] += 1
            else:
                book[low_c] = 1

        def check(book, tmp):
            for k, v in book.items():
                if k not in tmp:
                    return False
                if tmp[k] < v:
                    return False
            return True

        min_len, min_word = float('inf'), ''
        for word in words:
            tmp = {}
            for c in word:
                if c in tmp:
                    tmp[c] += 1
                else:
                    tmp[c] = 1
            if check(book, tmp):
                if len(word) < min_len:
                    min_len = len(word)
                    min_word = word

        return min_word

s = Solution()
print(s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))