from typing import Optional, ListNode

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKNode(self, head, k):
        cur = head
        prev_node = None
        for _ in range(k):
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
        return prev_node, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        runner = head
        prev_chunk_tail = dummy
        while True:
            chunk_head = runner
            for _ in range(k):
                if not runner:
                    return dummy.next
                runner = runner.next
            chunk_top, chunk_tail = self.reverseKNode(chunk_head, k)
            prev_chunk_tail.next = chunk_top
            chunk_tail.next = runner
            prev_chunk_tail = chunk_tail
