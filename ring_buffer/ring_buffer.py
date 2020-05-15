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
        if self.extra >= self.capacity:
            new_node = Node(item)
            current = self.head
            self.head = new_node
            print(self.capacity, current.value, "????")
            new_node.set_next(current)

            for i in range(0, self.capacity - 2):
                current = current.get_next()
                # print("11111", current.get_value())
            current.set_next(None)

            self.head = new_node
            print(self.extra, "I MADE IT")

            return
        elif self.size < self.capacity:
            self.size += 1
            new_node = Node(item)
            if not self.head:
                # print("IN HERE")
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
            print(self.extra, current.value, "EXTRA")
            if self.extra <= 1:
                print("SHOULD ONLY BE 1")

                new_node.set_next(current.get_next())
                self.head = new_node
                # print(
                #     current.value,
                #     range(self.extra),
                #     self.head.value,
                #     "OUTSIDE ELSE"
                # )
                return

            else:
                # self.head = new_node
                # self.head.set_next(None)
                print(
                    range(self.extra),
                    self.head.value,
                    self.head.get_next().value,
                    new_node.value,
                    current.get_next().get_next().value,
                    # new_node.get_next().value,
                    # new_node.get_next().get_next().value,
                    "IN ELSE "
                )

                # self.head.set_next(current.get_next())
                a = self.head
                for num in range(self.extra - 2):
                    current = current.get_next()
                    # print(current.value, "IN FOR CURRENT")
                for num in range(self.extra):
                    a = a.get_next()
                    print("LOOP")
                # print(a.get_value(), current.get_next().value, "IN FOR")
                new_node.set_next(a)
                current.set_next(new_node)
                # self.head.set_next(current)

                print(self.head.get_next().value, "HAIL MARY")
                if self.capacity == self.extra:
                    self.extra = 0

                # while current.get_next() is not None:
                #     if current.get_next().get_value() == a.get_value():
                #         d = current.get_next().get_next()
                #         current.set_next(d)
                #         print(current.get_value(), "IN WHILE")
                #     else:
                #         current = current.get_next()

                # self.head.set_next(new_node)
                # 11 needs to kill 101 and keep 4   12
                # needs to kill 105 and keep 11 , 4
            # if self.extra == self.capacity:
            #     self.extra = 0
            #     print(self.extra, "I MADE IT")

    def get(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next_node
        return nodes


if __name__ == "__main__":

    l = RingBuffer(5)

    # l.append('a')

    l.append('a')
    l.append('b')
    l.append('c')
    l.append('d')
    print(l.get(), "BEFORE FULL:", l.__len__())
    l.append('e')
    print(l.get(), "Length2:", l.__len__())
    l.append('f')
    print(l.get(), "Length2:", l.__len__())
    l.append('g')
    print(l.get(), "Length2:", l.__len__())
    l.append('h')
    print(l.get(), "Length2:", l.__len__())
    l.append('i')
    print(l.get(), "Length2:", l.__len__())
    l.append('j')
    print(l.get(), "Length2:", l.__len__())
    l.append("k")
    print(l.get(), "Length2:", l.__len__())

    # l.append(11)
    # l.append(16)

    # l.append(19)
    # l.append(119)
    # l.append(2219)
    # print(l.get(), "Length2:", l.__len__())
    # l.append(3311)
    # print(l.get(), "Length2:", l.__len__())
    # l.append(4419)
    # print(l.get(), "Length2:", l.__len__())
    # # ITS BROKEN STILL
