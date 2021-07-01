class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
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
                    serialize_val.append('#')
            if tmp_level: queue.append(tmp_level)
        while serialize_val and serialize_val[-1] == '#':
            serialize_val.pop()
        return serialize_val

    def deserialize(self, data):
        if not data: return None
        root = TreeNode(data.pop(0))
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            tmp_level = []
            while level:
                node = level.pop(0)
                if data:
                    val = data.pop(0)
                    if val != '#':
                        node.left = TreeNode(val)
                        tmp_level.append(node.left)
                if data:
                    val = data.pop(0)
                    if val != '#':
                        node.right = TreeNode(val)
                        tmp_level.append(node.right)
            if tmp_level: queue.append(tmp_level)
        return root