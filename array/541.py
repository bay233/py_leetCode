# 541. 反转字符串 II

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_len = len(s)
        s_list = list(s)
        low, fast = 0, k - 1

        def s_remove(l, r):
            while l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1

        while fast < s_len:
            s_remove(low, fast)
            low += 2 * k
            fast += 2 * k

        s_remove(low, s_len - 1)

        return "".join(s_list)


s = Solution()
print(s.reverseStr(s="abcdefg", k=2))
