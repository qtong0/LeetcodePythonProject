class Solution(object):
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        res = []
        self.dfs("0" * (n-1), k, seen, res)
        return "".join(res) + "0" * (n-1)

    def dfs(self, node, k, seen, res):
        for i in range(k):
            s = str(i)
            nei = node + s
            if nei not in seen:
                seen.add(nei)
                self.dfs(nei[1:], k, seen, res)
                res.append(s)



    def crackSafe_DFS(self, n, k):
        total = k**n
        arr = ['0']*n
        visited = set(['0'*n])
        self.dfs2(arr, total, visited, n, k)
        return ''.join(arr)
    
    def dfs2(self, arr, goal, visited, n, k):
        if len(visited) == goal: return True
        prevArr = arr[len(arr)-n+1:]
        for i in range(k):
            nextArr = prevArr+[str(i)]
            nextStr = ''.join(nextArr)
            if nextStr not in visited:
                visited.add(nextStr)
                arr.append(str(i))
                if self.dfs2(arr, goal, visited, n, k):
                    return True
                visited.remove(nextStr)
                arr.pop()
        return False
    
    def test(self):
        testCases = [
            [1, 2],
            [2, 2],
        ]
        for n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.crackSafe(n, k)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
