# 725. 分隔链表

List = list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        res = [None] * k
        node = head
        count = 0
        while node:
            count += 1
            node = node.next

        l, r = head, head
        for i in range(k):
            num = k - i
            avg = count // num + 1 if count % num else count // num
            j = 1
            while r and j < avg:
                r = r.next
                j += 1
            res[i] = l
            if r:
                l = r.next
                r.next = None
                r = l
            else:
                l = r
            count -= avg

        return res


def createHead(arr, i=0):
    if i >= len(arr): return None
    return ListNode(arr[i], createHead(arr, i + 1))


head = createHead([1,2,3,4,5,6,7])

s = Solution()
res = s.splitListToParts(head, 3)
print(res)
