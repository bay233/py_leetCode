# 450. 删除二叉搜索树中的节点

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def delete(root: TreeNode, key: int):
            if not root: return None
            if key > root.val:
                root.right = delete(root.right, key)
            elif key < root.val:
                root.left = delete(root.left, key)
            else:
                if root.left and root.right:
                    root.val = root.right.val
                    node = self.maxNode(root.left)
                    node.right = root.right.left
                    root.right = root.right.right
                elif not root.left and root.right:
                    root.val = root.right.val
                    node = root.right
                    root.right = node.right
                    root.left = node.left
                elif not root.right and root.left:
                    root.val = root.left.val
                    node = root.left
                    root.left = node.left
                    root.right = node.right
                else:
                    root = None
            return root
        return delete(root, key)

    def maxNode(self, root):
        if not root.right: return root
        return self.maxNode(root.right)


def printTree(root: TreeNode):
    if not root: return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(8)
right = root.right
right.right = TreeNode(10)
right.right.right = TreeNode(12)
right.right.right.right = TreeNode(14)

'''
        5
    1       8
                10
                    12
'''

s = Solution()
printTree(s.deleteNode(root, 8))
