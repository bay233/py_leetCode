# 429. N 叉树的层序遍历

List = list


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        q = [[root]]
        while q:
            lv = q.pop(0)
            level = []
            tmp = []
            for n in lv:
                if not n:
                    continue
                level.append(n.val)
                if n.children:
                    tmp += n.children
            if level:
                ans.append(level)
            if tmp:
                q.append(tmp)
        return ans
