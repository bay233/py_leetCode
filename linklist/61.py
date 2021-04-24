# 61. 旋转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        def getNode(head, k):
            size = 1
            tail = head
            node = head
            tmp_k = k
            while tail.next:
                if tmp_k <= 0:
                    node = node.next
                tmp_k -= 1
                tail = tail.next
                size += 1
            return size, node, tail

        size, node, tail = getNode(head, k)
        if k >= size:
            size, node, tail = getNode(head, k % size)

        print(size, node.val, tail.val)
        tail.next = head
        head = node.next
        node.next = None
        return head

s = Solution()
head = ListNode(1)
node = head
for i in range(2, 6):
    node.next = ListNode(i)
    node = node.next
node = head
while node:
    print(node.val)
    node = node.next
print()
node = s.rotateRight(head, 3)
while node:
    print(node.val)
    node = node.next