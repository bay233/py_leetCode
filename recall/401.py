# 401. 二进制手表

class Solution:
    # def readBinaryWatch(self, turnedOn: int) -> List[str]:
    def readBinaryWatch(self, turnedOn: int):
        if turnedOn > 8: return []
        hour = [['0'], ['1', '2', '4', '8'], ['3', '5', '9', '6', '10'], ['7', '11']]
        minute = [['00'], ['32', '01', '02', '04', '08', '16'],
                  ['33', '34', '03', '36', '05', '06', '40', '09', '10', '12', '48', '17', '18', '20', '24'],
                  ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49',
                   '50', '52', '56'],
                  ['39', '43', '45', '46', '15', '51', '53', '54', '23', '57', '58', '27', '29', '30'],
                  ['55', '59', '47', '31']]

        h = turnedOn if turnedOn <= 3 else 3
        res = []
        for i in range(h + 1):
            m = turnedOn - i
            if m > 5: continue
            for hstr in hour[i]:
                for mstr in minute[m]:
                    res.append(hstr + ":" + mstr)
        return res


s = Solution()
print(s.readBinaryWatch(1))
