# 116. 填充每个节点的下一个右侧节点指针

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        def dp(root1: 'Node', root2: 'Node'):
            if not root1 or not root2: return

            root1.next = root2
            dp(root1.left, root1.right)
            dp(root2.left, root2.right)
            dp(root1.right, root2.left)
        dp(root.left, root.right)
        return root

    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return root
    #     nodes = [root]
    #     while len(nodes):
    #         t = []
    #         tmpNode = None
    #         for node in nodes:
    #             if node.left and node.right:
    #                 t.append(node.left)
    #                 t.append(node.right)
    #             if tmpNode:
    #                 tmpNode.next = node
    #             tmpNode = node
    #         nodes = t
    #     return root