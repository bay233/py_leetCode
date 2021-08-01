# 1104. 二叉树寻路

class Solution:
    # def pathInZigZagTree(self, label: int) -> List[int]:
    def pathInZigZagTree(self, label: int):
        cur, pre = 0, 0
        n = 0
        for i in range(1, 100):
            cur, pre = 2 ** i - 1, cur
            if pre < label <= cur:
                n = i
                break
        res = [1]
        l, r = 1, 1
        m = 1
        while m < n:
            mid = (cur + pre) // 2
            if n & 1:
                if mid >= label:
                    cur = mid
                    if m & 1:
                        res.append(r * 2 + 1)
                    else:
                        res.append(l * 2)
                    l = l * 2
                    r = r * 2 + 1
                else:
                    pre = mid
                    if m & 1:
                        res.append(r * 2)
                    else:
                        res.append(l * 2 + 1)
                    l = l * 2 + 1
                    r = r * 2
            else:
                if mid >= label:
                    cur = mid
                    if m & 1:
                        res.append(l * 2)
                    else:
                        res.append(r * 2 + 1)
                    l = l * 2
                    r = r * 2 + 1
                else:
                    pre = mid
                    if m & 1:
                        res.append(l * 2 + 1)
                    else:
                        res.append(r * 2)
                    l = l * 2 + 1
                    r = r * 2
            m += 1
        return res

s = Solution()
print(s.pathInZigZagTree(656356))