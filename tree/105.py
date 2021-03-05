# 105. 从前序与中序遍历序列构造二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not len(inorder): return None
        val = preorder.pop(0)
        index = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root



def printTree(root: TreeNode):
    if not root: return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

s = Solution()
printTree(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))