# 1418. 点菜展示表

class Solution:
    # def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
    def displayTable(self, orders):
        menu_dirc = {}
        users = set()
        for order in orders:
            if order[2] in menu_dirc:
                menu = menu_dirc[order[2]]
                if order[1] in menu:
                    menu[order[1]] += 1
                else:
                    menu[order[1]] = 1
            else:
                menu_dirc[order[2]] = dict()
                menu_dirc[order[2]][order[1]] = 1
            if order[1] not in users:
                users.add(order[1])
        menus = list(menu_dirc.keys())
        menus.sort()
        head = ['Table'] + menus
        users = list(users)
        users.sort(key=lambda x: int(x))
        print(menu_dirc)
        res = [head]
        for u in users:
            tmp = [u]
            for m in menus:
                if u in menu_dirc[m]:
                    tmp.append(str(menu_dirc[m][u]))
                else:
                    tmp.append('0')
            res.append(tmp)
        return res


s = Solution()
print(s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                      ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
