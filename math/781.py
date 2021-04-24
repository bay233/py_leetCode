# 781. 森林中的兔子

class Solution:
    def numRabbits(self, answers) -> int:
        book = {}
        count = 0
        for answer in answers:
            if answer in book:
                book[answer] += 1
                if book[answer] > answer + 1:
                    book[answer] = 1
                    count += answer + 1
            else:
                book[answer] = 1
                count += answer + 1
        return count

s = Solution()

print(s.numRabbits([10, 10, 10]))