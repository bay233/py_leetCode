# 449. 序列化和反序列化二叉搜索树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        serialize_val = []
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            tmp_level = []
            while level:
                node = level.pop(0)
                if node:
                    serialize_val.append(node.val)
                    tmp_level.append(node.left)
                    tmp_level.append(node.right)
                else:
                    serialize_val.append(None)
            if tmp_level: queue.append(tmp_level)
        while serialize_val and serialize_val[-1] == None:
            serialize_val.pop()
        if serialize_val:
            tmp = []
            for i in serialize_val:
                if i is None:
                    tmp.append('null')
                    continue
                tmp.append(str(i))
            serialize_val = tmp

        return ",".join(serialize_val)

    def deserialize(self, data: str) -> TreeNode:
        if not data: return None
        data = data.split(",")
        tmp = []
        for i in data:
            if i == 'null':
                tmp.append(None)
                continue
            tmp.append(int(i))
        data = tmp
        root = TreeNode(data.pop(0))
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            tmp_level = []
            while level:
                node = level.pop(0)
                if data:
                    val = data.pop(0)
                    if val != None:
                        node.left = TreeNode(val)
                        tmp_level.append(node.left)
                if data:
                    val = data.pop(0)
                    if val != None:
                        node.right = TreeNode(val)
                        tmp_level.append(node.right)
            if tmp_level: queue.append(tmp_level)
        return root


c = Codec()
d = c.deserialize(','.join(['2', '1', '3']))
print(d)
ans = c.serialize(d)
print(ans)
