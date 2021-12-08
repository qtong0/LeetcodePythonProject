from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.tree = [[] for _ in parent]
        for i, x in enumerate(parent):
            if x != -1: self.tree[x].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked: return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user: return False
        self.locked.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked: return False # check for unlocked

        node = num
        while node != -1:
            if node in self.locked: break # locked ancestor
            node = self.parent[node]
        else:
            stack = [num]
            descendant = []
            while stack:
                node = stack.pop()
                if node in self.locked: descendant.append(node)
                for child in self.tree[node]: stack.append(child)
            if descendant:
                self.locked[num] = user # lock given node
                for node in descendant: self.locked.pop(node) # unlock all descendants
                return True
        return False # locked ancestor


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


if __name__ == '__main__':
    # ["LockingTree","lock","unlock","unlock","lock","upgrade","lock"]
    # [[[-1,0,0,1,1,2,2]],[2,2],[2,3],[2,2],[4,5],[0,1],[0,1]]
    #
    obj = LockingTree([-1,0,0,1,1,2,2])
    print(obj.lock(2,2))
    print(obj.unlock(2,3))
    print(obj.unlock(2,2))
    print(obj.lock(4,5))
    print(obj.upgrade(0,1))
    print(obj.lock(0,1))


    # ["LockingTree","upgrade","upgrade","upgrade","unlock","upgrade"]
    # [[[-1,0,3,0,3]],[4,1],[3,2],[0,5],[3,3],[2,1]]
    #
    # obj = LockingTree([-1,0,3,0,3])
    # print(obj.upgrade(4,1))
    # print(obj.upgrade(3,2))
    # print(obj.upgrade(0,5))
    # print(obj.unlock(3,3))
    # print(obj.upgrade(2,1))


    # ["LockingTree","upgrade","upgrade","upgrade","upgrade","unlock","unlock","upgrade","upgrade","upgrade","lock","lock","upgrade","upgrade","unlock","upgrade","upgrade","upgrade","upgrade","unlock","unlock"]
    # [[[-1,6,5,5,7,0,7,0,0,6]],[5,3],[2,3],[7,39],[1,32],[5,44],[2,15],[1,11],[1,18],[3,7],[5,36],[5,42],[8,5],[1,19],[3,38],[0,27],[4,11],[9,2],[8,41],[5,36],[7,29]]
    #
    # obj = LockingTree([-1,6,5,5,7,0,7,0,0,6])
