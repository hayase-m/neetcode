from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        while cur_node:
            tmp_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = tmp_node
        return prev_node


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

print(Solution().reverseList(node1).val)
