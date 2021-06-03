# 1734. 解码异或后的排列

class Solution:
    # def decode(self, encoded: List[int]) -> List[int]
    def decode(self, encoded):
        en_xor = encoded[0]
        for i in range(2, len(encoded), 2):
            en_xor ^= encoded[i]
        res_xor = 1
        for i in range(2, len(encoded) + 2):
            res_xor ^= i
        tmp = en_xor ^ res_xor
        res = [tmp]
        while encoded:
            tmp ^= encoded.pop()
            res.append(tmp)
        res.reverse()
        return res


s = Solution()
print(s.decode([6, 5, 4, 6]))
