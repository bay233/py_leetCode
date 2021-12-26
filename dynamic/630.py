# 630. 课程表 III

from sortedcontainers import sortedlist

List = list


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[-1])
        q = sortedlist.SortedList(key=lambda x: -x)
        res = 0
        for course in courses:
            d, e = course[0], course[1]
            res += d
            q.add(d)
            if res > e:
                res -= q.pop(0)
        return len(q)


s = Solution()
print(s.scheduleCourse([[5,5],[4,6],[2,6]]))
