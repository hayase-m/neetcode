

class Node:
    def __init__(self, key=None, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.node_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def delete_node(self, target_node: Node):
        target_node.prev.next = target_node.next
        target_node.next.prev = target_node.prev

    def add_tail(self, target_node: Node):
        prev = self.tail.prev
        prev.next = target_node
        target_node.prev = prev
        target_node.next = self.tail
        self.tail.prev = target_node

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        target_node = self.node_map[key]
        self.delete_node(target_node)
        self.add_tail(target_node)

        return target_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.node_map[key].val = value
            self.delete_node(self.node_map[key])
            self.add_tail(self.node_map[key])
        else:
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.add_tail(new_node)

        if self.cap < len(self.node_map):
            target_key = self.head.next.key
            self.node_map.pop(target_key)
            self.delete_node(self.head.next)
