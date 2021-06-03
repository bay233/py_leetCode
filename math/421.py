# 421. 数组中两个数的最大异或值

class Trie:
    def __init__(self, left = None, rigth=None):
        self.left = left
        self.rigth = rigth


class Solution:
    # def findMaximumXOR(self, nums: List[int]) -> int:
    def findMaximumXOR(self, nums) -> int:
        # 取得最大长度
        L = len(format(max(nums), 'b')) - 1
        root = Trie()
        for num in nums:
            curr = root
            for i in range(L, -1, -1):
                v = (num >> i) & 1
                if v:
                    if curr.left == None:
                        curr.left = Trie()
                    curr = curr.left
                else:
                    if curr.rigth == None:
                        curr.rigth = Trie()
                    curr = curr.rigth

        res = 0
        for num in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1):
                v = (num >> i) & 1
                if v:
                    if curr.rigth != None:
                        total = total*2 + 1
                        curr = curr.rigth
                    else:
                        total = total*2
                        curr = curr.left
                else:
                    if curr.left != None:
                        total = total * 2 + 1
                        curr = curr.left
                    else:
                        total = total * 2
                        curr = curr.rigth
            res = max(res, total)
        return res


s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
