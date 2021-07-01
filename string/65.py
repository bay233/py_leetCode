# 65. 有效数字

class Solution:

    def isNumber(self, s: str) -> bool:
        numbers = [str(_) for _ in range(10)]
        def isNum(s):
            if not s: return False
            for word in s:
                if word not in numbers:
                    return False
            return True

        def isFloat(s):
            if '.' in s:
                ss_f = s.split('.')
                if len(ss_f) != 2: return False
                if ss_f[0] and ss_f[0][0] in ['+', '-']:
                    ss_f[0] = ss_f[0][1:]
                if ss_f[0] == '' and ss_f[1] == '':
                    return False
                elif not ss_f[0]:
                    return isNum(ss_f[1])
                elif not ss_f[1]:
                    return isNum(ss_f[0])
                else:
                    return isNum(ss_f[0]) and isNum(ss_f[1])
            else:
                if s and s[0] in ['+', '-']:
                    return isNum(s[1:])
                else:
                    return isNum(s)

        if 'e' in s or 'E' in s:
            ss_e = []
            if 'e' in s:
                ss_e = s.split('e')
            if 'E' in s:
                ss_e = s.split('E')
            if len(ss_e) != 2: return False
            if ss_e[0] == '' or ss_e[1] == '': return False
            res1 = isFloat(ss_e[0][1:]) if ss_e[0] and ss_e[0][0] in ['+', '-'] else isFloat(ss_e[0])
            res2 = isNum(ss_e[1][1:]) if ss_e[1] and ss_e[1][0] in ['+', '-'] else isNum(ss_e[1])
            return res1 and res2
        else:
            return isFloat(s)




s = Solution()
print(s.isNumber(s = "+.8"))