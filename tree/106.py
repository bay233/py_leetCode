# 106. 从中序与后序遍历序列构造二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if not len(inorder): return None
        val = postorder.pop()
        ino_index = inorder.index(val)
        root = TreeNode(val)
        root.right = self.buildTree(inorder[ino_index + 1:], postorder)
        root.left = self.buildTree(inorder[:ino_index], postorder)
        return root

def printTree(root: TreeNode):
    if not root: return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

s = Solution()
printTree(s.buildTree([1,2,3],[3,2,1]))