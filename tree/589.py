# 589. N 叉树的前序遍历


List = list


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for node in root.children:
            ans += self.preorder(node)
        return [root.val] + ans

