# 297. 二叉树的序列化与反序列化

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        return [root.val] + self.serialize(root.left) + self.serialize(root.right) if root else [None]

    def deserialize(self, data):
        def do(data):
            if not len(data): return None
            val = data.pop(0)
            if val != None:
                root = TreeNode(val)
                root.left = do(data)
                root.right = do(data)
                return root
            else:
                return None
        return do(data)


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

ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize([5, 1, None, None, 8, None, 10, None, 12, None, 14, None, None])
print(ans)
printTree(ans)
