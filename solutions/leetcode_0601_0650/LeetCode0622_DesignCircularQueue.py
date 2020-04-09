class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        # empty queue
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularQueue_own:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == self.maxSize:
            return False
        else:
            self.size += 1
            if not self.head:
                self.head = self.tail = Node(value)
            else:
                node = Node(value)
                self.tail.next = node
                self.tail = node
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        if self.size == 1:
            self.size = 0
            self.head = self.tail = None
        else:
            self.size -= 1
            nextNode = self.head.next
            nextNode.prev = None
            self.head = nextNode
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return not self.size

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

if __name__ == '__main__':
    # circularQueue = MyCircularQueue(3);     # set the size to be 3
    # print(circularQueue.enQueue(1))         # return true
    # print(circularQueue.enQueue(2))         # return true
    # print(circularQueue.enQueue(3))         # return true
    # print(circularQueue.enQueue(4))         # return false, the queue is full
    # print(circularQueue.Rear())             # return 3
    # print(circularQueue.isFull())           # return true
    # print(circularQueue.deQueue())          # return true
    # print(circularQueue.enQueue(4))         # return true
    # print(circularQueue.Rear())             # return 4

    circularQueue = MyCircularQueue(6)
    print(circularQueue.enQueue(6))
    print(circularQueue.Rear())
    print(circularQueue.Rear())
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(5))
    print(circularQueue.Rear())
    print(circularQueue.deQueue())
    print(circularQueue.Front())
    print(circularQueue.deQueue())
    print(circularQueue.deQueue())
    print(circularQueue.deQueue())
