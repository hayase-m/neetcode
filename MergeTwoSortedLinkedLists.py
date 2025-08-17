from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode()
        cur_node = dummy

        while l1 and l2:
            if l1.val >= l2.val:
                cur_node.next = l2
                l2 = l2.next
            else:
                cur_node.next = l1
                l1 = l1.next
            cur_node = cur_node.next
        cur_node.next = l1 or l2
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(5)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

print(Solution().mergeTwoLists(node1, node4).val)
