# 341. 扁平化嵌套列表迭代器

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       return True

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       return 0

   def getList(self) -> list:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       return list(self)


class NestedIterator(object):
    falt_data = []
    index = 0

    def __init__(self, nestedList: [NestedInteger]):
        def do(nestedList):
            res = []
            for nested in nestedList:
                if nested.isInteger():
                    res.append(nested.getInteger())
                else:
                    res += do(nested.getList())
            return res
        self.falt_data = do(nestedList)


    def next(self):
        val = self.falt_data[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.falt_data)
