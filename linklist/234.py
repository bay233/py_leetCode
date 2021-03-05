# 234. 回文链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head

        def recall(head):
            if not head: return True
            res = recall(head.next)
            if not res: return res
            left = self.left.val
            right = head.val
            if left == right:
                self.left = self.left.next
            else:
                res = False
            return res
        return recall(head)

s = Solution()
print(s.isPalindrome())