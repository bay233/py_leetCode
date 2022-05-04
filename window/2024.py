# 2024. 考试的最大困扰度

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def getCnt(c):
            ans = 0
            cnt = 0
            j = 0
            for i in range(k):
                if answerKey[i] == c:
                    cnt += 1
                while cnt > k:
                    if answerKey[j] == c:
                        cnt -= 1
                ans = max(ans, i - j + 1)
            return ans
        n = len(answerKey)
        return max(getCnt('T'), getCnt('F'))
