from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, head1, head2):
        dummy = ListNode()
        cur1 = head1
        cur2 = head2
        cur = dummy

        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next
            cur = cur.next
        cur.next = cur1 if cur1 else cur2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i - 1])
        return lists[i]
