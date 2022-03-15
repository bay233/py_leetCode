# 846. 一手顺子


List = list

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        hand.sort()
        while hand:
            v = hand[0]
            hand.pop(0)
            i = 0
            n = len(hand)
            for j in range(1, groupSize):
                while i < n and v == hand[i]:
                    i += 1
                if i == n or hand[i] - v != 1:
                    return False
                v = hand[i]
                hand.pop(i)
        return True

s = Solution()
print(s.isNStraightHand(hand = [1,1,2,2,3,3], groupSize = 2))

