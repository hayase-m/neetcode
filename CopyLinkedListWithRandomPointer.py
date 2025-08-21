from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        node_map[None] = None
        cur_old = head
        while cur_old:
            new_node = Node(cur_old.val)
            node_map[cur_old] = new_node
            cur_old = cur_old.next
        cur_old = head
        while cur_old:
            cur_new = node_map[cur_old]
            cur_new.next = node_map[cur_old.next]
            cur_new.random = node_map[cur_old.random]
            cur_old = cur_old.next
        return node_map[head]
