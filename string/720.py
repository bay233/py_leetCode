# 720. 词典中最长的单词

List = list


class Solution:
    def longestWord(self, words: List[str]) -> str:
        book = set()
        for w in words:
            book.add(w)

        words.sort(key=lambda x: len(x), reverse=True)

        def check(w):
            for i in range(1, len(w)):
                if w[:-i] not in book:
                    return False
            return True

        n = -1
        ans = []
        for w in words:
            if n != -1 and n != len(w):
                break
            if check(w):
                n = len(w)
                ans.append(w)
        ans.sort()

        return ans[0] if len(ans) > 0 else ''

s = Solution()
print(s.longestWord(["w","wo","wor","worl"]))