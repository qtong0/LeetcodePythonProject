import random


class Node:
    def __init__(self, val, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class Skiplist:

    def __init__(self):
        self.head = Node(-1)


    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.right and curr.right.val < target:
                curr = curr.right
            if curr.right and curr.right.val == target:
                return True
            curr = curr.down
        return False


    def add(self, num: int) -> None:
        stack = []
        curr = self.head
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            stack.append(curr)
            curr = curr.down
        insert = True
        down = None
        while insert and stack:
            curr = stack.pop()
            curr.right = Node(num, curr.right, down)
            down = curr.right
            insert = random.random() < 0.5
        if insert:
            self.head = Node(-1, None, self.head)


    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            if curr.right and curr.right.val == num:
                found = True
                curr.right = curr.right.right
            curr = curr.down
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


if __name__ == '__main__':
    sl = Skiplist()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    print(sl.search(0))
    sl.add(4)
    print(sl.search(1))
    sl.erase(0)
    sl.erase(1)
    print(sl.search(1))
