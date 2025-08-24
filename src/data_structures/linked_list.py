"""Linked List module."""

# -- Imports

from typing import Generic, Iterator, Optional, TypeVar

# --

T = TypeVar("T")


class Node(Generic[T]):
    """Single Linked List Node for data object."""

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None


class SinglyLinkedList(Generic[T]):
    """Single linked-list class.

    Methods:
        __init__() -> None
            - Initializes an empty linked list.

        __len__() -> int
            - Returns the number of elements in the list.

        __iter__() -> Iterator[T]
            - Iterates over the values in the list.

        __repr__() -> str
            - Returns a string representation of the list.

        push(value) -> None
            - Adds a value to the front of the list.

        append(value) -> None
            - Adds a value to the end of the list.

        shift() -> Optional[T]
            - Removes and returns the first element of the list.

        pop() -> Optional[T]
            - Removes and returns the last element of the list.

        find(value) -> bool
            - Checks if a value exists in the list.

        insert(value, idx) -> None
            - Inserts a value at the specified index.

        erase(value) -> bool
            - Removes the first occurrence of a value from the list.

    """

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return " -> ".join(str(v) for v in self) + " -> None"

    def push(self, value: T) -> None:
        """Adds a value to the top of the list."""

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def append(self, value: T) -> None:
        """Adds a value to the back of the list."""

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def shift(self) -> Optional[T]:
        """Deletes the value from the top of the list and returns it."""

        current = self.head
        if current:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return current.value

        return None

    def pop(self) -> Optional[T]:
        """Deletes the value from the back of the list and returns it."""

        if not self.head:
            return None

        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.size -= 1
            return value

        current = self.head
        while current.next != self.tail:
            current = current.next

        value = self.tail.value
        current.next = None
        self.tail = current
        self.size -= 1
        return value

    def find(self, value: T) -> bool:
        """Searches for a value in the list."""

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert(self, value: T, idx: int) -> None:
        """Insert the value into the list at the specified index."""

        if idx < 0 or idx > len(self):
            raise IndexError("Index out of range")

        if idx == 0:
            self.push(value)
            return

        if len(self) == idx:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(idx - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def erase(self, value: T) -> bool:
        """Deletes a value from the list if it exists."""

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

                self.size -= 1
                return True

            prev = current
            current = current.next

        return False


# --


__all__ = [
    "Node",
    "SinglyLinkedList",
]
