class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.maxSize = k
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size == self.maxSize:
            return False
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size == self.maxSize:
            return False
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        else:
            self.size -= 1
            if self.size == 0:
                self.head = self.tail = 0
            else:
                node = self.head.next
                self.head = node
                self.head.prev = None
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        else:
            self.size -= 1
            if self.size == 0:
                self.head = self.tail = 0
            else:
                node = self.tail.prev
                self.tail = node
                self.tail.next = None
            return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
