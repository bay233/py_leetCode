# 173. 二叉搜索树迭代器

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.point = 0
        self.queue = []
        self.__getItem(root)

    def __getItem(self, root: TreeNode):
        if not root: return
        self.__getItem(root.left)
        self.queue.append(root.val)
        self.__getItem(root.right)

    def next(self) -> int:
        res = self.queue[self.point]
        self.point += 1
        return res

    def hasNext(self) -> bool:
        return self.point < len(self.queue)
