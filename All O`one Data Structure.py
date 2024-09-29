class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()  # A set of keys with this count
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_count = {}  # Maps key to its count
        self.count_nodes = {}  # Maps count to the corresponding Node
        self.head = Node(float('-inf'))  # Dummy head with very low count
        self.tail = Node(float('inf'))   # Dummy tail with very high count
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node: Node, prev_node: Node):
        # Insert new_node after prev_node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node: Node):
        # Remove the node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key: str) -> None:
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count + 1
            self.key_count[key] = new_count
            # Move the key to the next node in the linked list
            current_node = self.count_nodes[current_count]
            current_node.keys.remove(key)

            if new_count not in self.count_nodes:
                new_node = Node(new_count)
                self.count_nodes[new_count] = new_node
                self._add_node_after(new_node, current_node)

            self.count_nodes[new_count].keys.add(key)

            if len(current_node.keys) == 0:
                self._remove_node(current_node)
                del self.count_nodes[current_count]
        else:
            # New key, add with count 1
            self.key_count[key] = 1
            if 1 not in self.count_nodes:
                new_node = Node(1)
                self.count_nodes[1] = new_node
                self._add_node_after(new_node, self.head)
            self.count_nodes[1].keys.add(key)

    def dec(self, key: str) -> None:
        current_count = self.key_count[key]
        new_count = current_count - 1
        current_node = self.count_nodes[current_count]
        current_node.keys.remove(key)

        if new_count == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_count
            if new_count not in self.count_nodes:
                new_node = Node(new_count)
                self.count_nodes[new_count] = new_node
                self._add_node_after(new_node, current_node.prev)

            self.count_nodes[new_count].keys.add(key)

        if len(current_node.keys) == 0:
            self._remove_node(current_node)
            del self.count_nodes[current_count]

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
