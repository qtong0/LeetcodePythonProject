class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isleaf = False


class FileSystem:

    def __init__(self):
        self.root = TreeNode()

    def createPath(self, path: str, value: int) -> bool:
        node = self.root
        arr = path.split('/')[1:]
        for i, s in enumerate(arr):
            if i == len(arr) - 1:
                if s in node.children:
                    return False
                node.children[s] = TreeNode()
                node = node.children[s]
                node.isleaf = True
            elif s in node.children:
                node = node.children[s]
            else:
                return False
        if node.val or not node.isleaf:
            return False
        node.val = value
        return True

    def get(self, path: str) -> int:
        node = self.root
        for s in path.split('/')[1:]:
            if s in node.children:
                node = node.children[s]
            else:
                return -1
        if node.isleaf:
            return node.val
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


obj = FileSystem()
print(obj.createPath('/a', 1))
print(obj.get('/a'))
