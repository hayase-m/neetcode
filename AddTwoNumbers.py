from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode()
        dummy_head.next = l1
        l1_prev = dummy_head
        while (l1 and l2):
            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
            l1_prev = l1
            l1 = l1.next
            l2 = l2.next
        l1_prev.next = l1 or l2
        l1 = l1_prev.next
        while l1:
            carry, l1.val = divmod(l1.val + carry, 10)
            l1_prev = l1
            l1 = l1.next
        if (carry):
            l1_prev.next = ListNode(carry)

        return dummy_head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
node6.next = node7

result = Solution().addTwoNumbers(node1, node4)
while result:
    print(result.val)
    result = result.next
