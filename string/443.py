# 443. 压缩字符串

List = list


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("")
        low, fast = 0, 0
        count = 0
        res = 0
        while fast < len(chars):
            if chars[low] == chars[fast]:
                count += 1
            else:
                if count > 1:
                    c_str = str(count)
                    for c in c_str:
                        res += 1
                        low += 1
                        chars[low] = c
                low += 1
                chars[low] = chars[fast]
                res += 1
                count = 1
            fast += 1
        # print(chars)
        return res


s = Solution()
print(s.compress(["a","a","a","b","b","a","a"]))
