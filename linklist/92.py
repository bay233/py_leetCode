# 92. 反转链表 II

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(head, dis, depth):
            if not head.next: return head
            if depth >= dis:
                self.tail = head.next
                return head
            last = reverse(head.next, dis, depth + 1)
            head.next.next = head
            head.next = self.tail
            return last

        self.tail = None
        if m == 1:
            return reverse(head, n, 1)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

s = Solution()
head = ListNode(1)
node = head
for i in range(2, 5 + 1):
    node.next = ListNode(i)
    node = node.next


res = s.reverseBetween(head, 1, 3)
while res:
    print(res.val)
    res = res.next
