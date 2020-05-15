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


class RingBuffer:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0
        self.extra = 0

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def append(self, item):

        if self.size < self.capacity:
            self.size += 1
            new_node = Node(item)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.get_next() is not None:
                    current = current.get_next()
                current.set_next(new_node)
        else:
            self.extra += 1
            new_node = Node(item)
            current = self.head
            if self.extra <= 1:
                new_node.set_next(current.get_next())
                self.head = new_node
            else:
                a = self.head
                for num in range(self.extra - 2):
                    current = current.get_next()
                for num in range(self.extra):
                    a = a.get_next()
                new_node.set_next(a)
                current.set_next(new_node)
                if self.capacity == self.extra:
                    self.extra = 0

    def get(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next_node
        return nodes


if __name__ == "__main__":

    l = RingBuffer(4)

    l.append('a')
    l.append('b')
    l.append('c')
    l.append('d')
    print(l.get(), "FULL:", l.__len__())
    l.append('e')
    print(l.get(), "Length:", l.__len__())
    l.append('f')
    print(l.get(), "Length:", l.__len__())
    l.append('g')
    print(l.get(), "Length:", l.__len__())
    l.append('h')
    print(l.get(), "Length:", l.__len__())
    l.append('i')
    print(l.get(), "Length:", l.__len__())
    l.append('j')
    print(l.get(), "Length:", l.__len__())
    l.append("k")
    print(l.get(), "Length:", l.__len__())
