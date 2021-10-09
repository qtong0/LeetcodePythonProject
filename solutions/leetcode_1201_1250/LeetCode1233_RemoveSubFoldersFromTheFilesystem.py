from typing import List


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isleaf = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        res = []
        root = TreeNode()
        for f in folder:
            new_folder = False
            arr = f.split('/')
            node = root
            for i, dir in enumerate(arr):
                if dir != '':
                    if dir not in node.children:
                        new_folder = True
                        new_node = TreeNode(dir)
                        node.children[dir] = new_node
                        node = new_node
                    else:
                        node = node.children[dir]
                        if node.isleaf:
                            break
                    if i == len(arr)-1:
                        node.isleaf = True
            if new_folder:
                res.append(f)
        return res

    def test(self):
        test_cases = [
            ["/a","/a/b","/c/d","/c/d/e","/c/f"],
            ["/a","/a/b/c","/a/b/d"],
            ["/a/b/c","/a/b/ca","/a/b/d"],
        ]
        for folder in test_cases:
            res = self.removeSubfolders(folder)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
