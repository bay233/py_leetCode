# 25. K 个一组翻转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    tail = None

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, dis):
            if not head.next: return head
            if dis == 1:
                self.tail = head.next
                return head
            last = reverse(head.next, dis - 1)
            head.next.next = head
            head.next = self.tail
            return last

        dis = k
        node = head
        while dis:
            if not node:
                return head
            node = node.next
            dis -= 1
        newHead = reverse(head, k)
        head.next = self.reverseKGroup(node, k)
        return newHead

s = Solution()
head = ListNode(1)
node = head
for i in range(2, 5 + 1):
    node.next = ListNode(i)
    node = node.next


res = s.reverseKGroup(head, 3)
while res:
    print(res.val)
    res = res.next