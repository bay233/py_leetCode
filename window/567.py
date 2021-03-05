# 567. 字符串的排列

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = dict()
        neet = {}
        for _ in s1:
            if neet.get(_):
                neet[_] = neet[_] + 1
            else:
                neet[_] = 1
        left, right, valid = 0, 0, 0

        while right < len(s2):
            c = s2[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            if neet.get(c):
                if window[c] == neet.get(c):
                    valid += 1

            while right - left >= len(s1):
                if valid == len(neet):
                    return True
                d = s2[left]
                left += 1
                if neet.get(d):
                    if window[d] == neet[d]:
                        valid -= 1
                    window[d] = window[d] - 1
        return False


    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     window = dict()
    #     neet = {}
    #     for _ in s1:
    #         if neet.get(_):
    #             neet[_] = neet[_] + 1
    #         else:
    #             neet[_] = 1
    #     left, right, valid = 0, 0, 0
    #
    #     while right < len(s2):
    #         c = s2[right]
    #         right += 1
    #         window[c] = window.get(c, 0) + 1
    #         if window[c] == neet.get(c):
    #             valid += 1
    #
    #         while valid == len(neet):
    #             if len(s2[left:right]) == len(s1):
    #                 return True
    #             d = s2[left]
    #             left += 1
    #             if neet.get(d):
    #                 if window[d] == neet[d]:
    #                     valid -= 1
    #                 window[d] = window[d] - 1
    #     return False


s = Solution()
print(s.checkInclusion("ab", "eidboaoo"))