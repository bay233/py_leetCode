# 68. 文本左右对齐

List = list

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_len = len(words)
        word_count = 0
        cur_width = 0
        res = []
        tmp = []
        i = 0
        while i < words_len:
            w_len = len(words[i])
            cur_width += w_len
            word_count += 1
            tmp.append(words[i])
            i += 1

            if cur_width + word_count - 1 > maxWidth:
                tmp.pop()
                cur_width -= w_len
                word_count -= 1
                i -= 1
                line = ''
                space = maxWidth - cur_width
                while tmp:
                    if word_count - 1:
                        cur_space = space // (word_count - 1)
                        if space % (word_count - 1) != 0:
                            cur_space += 1
                    else:
                        cur_space = space
                    line += tmp.pop(0) + ' ' * cur_space
                    space -= cur_space
                    word_count -= 1
                cur_width = 0
                res.append(line)
            if i == words_len:
                line = ''
                space = maxWidth - cur_width - (word_count - 1)
                while tmp:
                    line += tmp.pop(0) + ' '
                res.append(line[:-1] + (' ' * space))
        return res

s = Solution()
print(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."],
maxWidth = 16
))





