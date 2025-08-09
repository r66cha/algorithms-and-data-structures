"""Linked List module"""


class Node:
    """Class Node for data object"""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """Single linked-list class"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        current = self.head
        self.head = new_node
        self.head.next = current
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def shift(self):
        current = self.head
        if current:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return current.value

    def pop(self):

        if not self.head:
            return None

        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.size -= 1
            return value

        current = self.head
        while current != self.tail:
            current = current.next

        value = self.tail.value
        current.next = None
        self.tail = current
        self.size -= 1
        return value

    def find(self, value):
        pass

    def index(self, idx):
        pass

    def insert(self, value, idx):
        new_node = Node(value)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return

        current = self.head
        current_idx = 0
        prev = 0

        while current and current_idx < idx:
            prev = current
            current = current.next
            current_idx += 1

        if current_idx == idx:
            prev.next = new_node
            new_node.next = current
            self.size += 1
        else:
            raise IndexError("Index out of range")

    def erase(self, value):
        current = self.head
        prev = None

        while current:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if prev.next is None:
                        self.tail = prev

                return True

            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("Finish")
