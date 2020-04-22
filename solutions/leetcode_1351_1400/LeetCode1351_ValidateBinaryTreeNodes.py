class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        graph = [[] for _ in range(n)]
        degree = [0]*n
        for i, node in enumerate(leftChild):
            if node != -1:
                graph[i].append(node)
                degree[node] += 1
                if degree[node] > 1:
                    return False
        for i, node in enumerate(rightChild):
            if node != -1:
                graph[i].append(node)
                degree[node] += 1
                if degree[node] > 1:
                    return False
        queue = []
        for node in range(n):
            if degree[node] == 0:
                queue.append(node)
        if len(queue) != 1:
            return False
        count = 1
        while queue:
            node = queue.pop(0)
            if len(graph[node]) > 2:
                return False
            for nextNode in graph[node]:
                degree[nextNode] -= 1
                if degree[nextNode] == 0:
                    queue.append(nextNode)
                    count += 1
        return count == n

    def test(self):
        testCases = [
            # [4, [1,-1,3,-1], [2,-1,-1,-1]],
            [4, [1,-1,3,-1], [2,3,-1,-1]],
            # [2, [1,0], [-1,-1]],
            # [6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]],
        ]
        for n, leftChild, rightChild in testCases:
            res = self.validateBinaryTreeNodes(n, leftChild, rightChild)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
