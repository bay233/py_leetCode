# 993. 二叉树的堂兄弟节点

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [[root]]
        while queue:
            nodes = queue.pop()
            level_node = []
            level_val = {}
            for node in nodes:
                if node.left:
                    level_node.append(node.left)
                    level_val[node.left.val] = node
                if node.right:
                    level_node.append(node.right)
                    level_val[node.right.val] = node
            if x in level_val and y in level_val and level_val[x] != level_val[y]:
                return True
            if level_node:
                queue.append(level_node)
        return False

s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.isCousins(root, 2, 3))