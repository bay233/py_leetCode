# 3. 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = right = 0
        reslen = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while window.get(c) > 1:
                d = s[left]
                window[d] = window[d] - 1
                left += 1

            reslen = max(reslen, right - left)

        return reslen


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
