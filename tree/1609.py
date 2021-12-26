# 1609. 奇偶树

from deserialize import deser

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: [TreeNode]) -> bool:
        q = [root]
        level = 0
        while q:
            tmp = []
            val = float('inf') if level & 1 else 0
            for n in q:
                v = n.val
                if level & 1:
                    if v & 1:
                        return False
                    if v >= val:
                        return False
                else:
                    if not v & 1:
                        return False
                    if v <= val:
                        return False
                val = v
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            q = tmp
            level += 1
        return True


null = None
c = deser.Codec()
s = Solution()
print(s.isEvenOddTree(c.deserialize([11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17])))