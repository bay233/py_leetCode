# 717. 1比特与2比特字符


List = list

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1]:
            return False

        n = len(bits)
        i = 0
        ans = 0
        while i < n:
            if bits[i]:
                ans = 1
                i += 2
                continue
            ans = 0
            i += 1
        return ans == 0

s = Solution()
print(s.isOneBitCharacter([1,1,1,0]))