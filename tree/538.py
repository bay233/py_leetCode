# 538. 把二叉搜索树转换为累加树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.tmp = 0
        def convert(root: TreeNode):
            if not root: return
            convert(root.right)
            root.val += self.tmp
            self.tmp = root.val
            convert(root.left)
        convert(root)
        return root


def printTree(root: TreeNode):
    if not root: return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s = Solution()
printTree(s.convertBST(root))