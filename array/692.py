# 692. 前K个高频单词

import functools
class Solution:
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    def topKFrequent(self, words, k: int):
        book = {}
        for word in words:
            if word in book:
                book[word] += 1
            else:
                book[word] = 1
        def sort_fun(x, y):
            if x[-1] == y[-1]:
                return -1 if x[0] > y[0] else 1
            else:
                return x[-1] - y[-1]
        res = sorted(book.items(), key=functools.cmp_to_key(sort_fun), reverse=True)
        return [_[0] for _ in res[:k]]


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],  3))