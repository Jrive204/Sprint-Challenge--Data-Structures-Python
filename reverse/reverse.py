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

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f'{node.value}')
            node = node.next_node
            # nodes.append(f"{node.value} ")
            # print(" -> ".join(nodes))
        return " -> ".join(nodes)

    def __len__(self):
        cur = self.head
        total = 0
        while cur is not None:
            total += 1
            cur = cur.next_node
        return f"Total in list: {total}"

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

    def reverse_list(self, node="start", prev=None):
        if node == "start":
            node = self.head
        if node:
            current = node.next_node
            node.next_node = prev
            self.reverse_list(current, node)
        else:
            self.head = prev


if __name__ == "__main__":

    llist = LinkedList()

    llist.add_to_head(1)
    llist.add_to_head(2)
    llist.add_to_head(10)
    print('\n', llist, '\n', llist.__len__())

    llist.reverse_list()
    print('\n After Reverse:----------\n\n', llist, '\n', llist.__len__())
