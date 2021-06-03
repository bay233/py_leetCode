# 690. 员工的重要性


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    # employees: List['Employee']
    def getImportance(self, employees, id: int) -> int:
        book = {}
        for employee in employees:
            book[employee.id] = [employee.importance, employee.subordinates]
        res = 0
        queue = [id]
        while queue:
            tmp_id = queue.pop(0)
            employee = book[tmp_id]
            res += employee[0]
            for i in employee[-1]:
                queue.append(i)
        return res


s = Solution()
print(s.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))
