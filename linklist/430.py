# 430. 扁平化多级双向链表

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def dp(node):
            if not node.next and not node.child:
                return node
            if node.child:
                child = node.child
                next_node = node.next
                node.next = child
                node.child = None
                child.prev = node
                node = dp(child)
                node.next = next_node
                if next_node:
                    next_node.prev = node
            if node.next:
                return dp(node.next)
            else:
                return node

        if head:
            node = head
            dp(node)
        return head


head = Node(1, None, None, Node(2, None, None, Node(3, None, None, None)))


s = Solution()
res = s.flatten(head)
print(res)
