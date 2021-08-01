# 面试题 10.02. 变位词组


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        book = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in book:
                book[sort_s].append(s)
            else:
                book[sort_s] = [s]
        return [v for k, v in book.items()]


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
