# 66. 加一

List = list


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        i = len(digits) - 1
        tmp = digits[i] + 1
        while i >= 0:
            if flag:
                tmp = digits[i] + 1
                flag = 0
            if tmp > 9:
                flag = 1
                digits[i] = 0
            else:
                digits[i] = tmp
                break
            i -= 1
        if flag:
            digits.insert(0, 1)
        return digits

s = Solution()
print(s.plusOne([9]))
