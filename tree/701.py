# 701. 二叉搜索树中的插入操作

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def doInsert(root: TreeNode, val: int):
            if not root: return None
            if val > root.val:
                node = doInsert(root.right, val)
                if not node:
                    root.right = TreeNode(val)
            if val < root.val:
                node = doInsert(root.left, val)
                if not node:
                    root.left = TreeNode(val)
            return root
        doInsert(root, val)
        return root if root else TreeNode(val)


def printTree(root: TreeNode):
    if not root: return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

s = Solution()
printTree(s.insertIntoBST(None, 2))
