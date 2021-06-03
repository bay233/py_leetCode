# 1720. 解码异或后的数组

class Solution:
    # def decode(self, encoded: List[int], first: int) -> List[int]:
    def decode(self, encoded, first: int):
        tmp = first
        res = []
        for n in encoded:
            res.append(tmp)
            tmp = tmp ^ n
        res.append(tmp)
        return res

s = Solution()
print(s.decode([1,2,3], 1))