# 1239. 串联字符串的最大长度

class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    def maxLength(self, arr) -> int:
        book = set()
        self.res_max = 0

        def chek(s):
            tmp_book = set()
            for ss in s:
                if ss in book or ss in tmp_book:
                    return False
                else:
                    tmp_book.add(ss)
            return True

        def dp(arr, index):
            if index >= len(arr): return
            for i in range(index, len(arr)):
                flag = False
                if chek(arr[i]):
                    flag = True
                    for s in arr[i]:
                        book.add(s)
                    self.res_max = max(self.res_max, len(book))
                dp(arr, i + 1)
                if flag:
                    for s in arr[i]:
                        book.remove(s)

        dp(arr, 0)
        return self.res_max


s = Solution()
print(s.maxLength(["yy","bkhwmpbiisbldzknpm"]))
