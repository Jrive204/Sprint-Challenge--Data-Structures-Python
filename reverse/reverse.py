class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def reverse_list(self, node, prev):
        if node is not None:
            current = node.next_node
            node.next_node = prev
            self.reverse_list(current, node)
        else:
            self.head = prev

    def length(self):
        cur = self.head
        total = 0
        while cur is not None:
            total += 1
            cur = cur.next_node
        return print(f"Total in list: {total}")

    def printList(self):
        cur = self.head
        if cur is None:
            return print("No items in list")
        else:
            while cur is not None:
                if cur.next_node is None:
                    print(f"{cur.value} -> None")
                    print(f"Head: {self.head.value}, Tail: {cur.next_node}")
                    return
                print(f"{cur.value} -> {cur.next_node.value}")
                cur = cur.next_node
