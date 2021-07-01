# 203. 移除链表元素

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        pre = ListNode(0, head)
        res = pre
        while node:
            if node.val == val:
                pre.next = node.next
            else:
                pre = node
            node = node.next
        return res.next

s = Solution()
vals = [1,2,6,3,4,5,6]
head = ListNode()
node = head
for i in vals:
    node.next = ListNode(i)
    node = node.next
print(s.removeElements(head.next,6))

