# 138. 复制带随机指针的链表

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node1 = head
        book1 = {}
        book2 = []
        head2 = Node(0)
        node2 = head2
        index = 0
        while node1:
            node2.next = Node(node1.val)
            book1[node1] = index
            index += 1
            node1 = node1.next
            node2 = node2.next
            book2.append(node2)
        head2 = head2.next
        node1 = head
        node2 = head2
        while node1:
            if node1.random:
                node2.random = book2[book1[node1.random]]
            node1 = node1.next
            node2 = node2.next
        return head2


node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1


s = Solution()
node = s.copyRandomList(node1)
while node:
    print(node.val, " ", node.next.val if node.next else None, " ", node.random.val if node.random else None)
    node = node.next

book = {}
book[None] = 1
print(book[None])