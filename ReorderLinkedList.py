from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        l1 = head
        l2 = prev

        while l1.next:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
        l1.next = l2


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(6)
node4 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4


head = node1

print(Solution().reorderList(head))
