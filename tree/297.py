# 297. 二叉树的序列化与反序列化

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return [root.val] + self.serialize(root.left) + self.serialize(root.right) if root else [None]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

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
