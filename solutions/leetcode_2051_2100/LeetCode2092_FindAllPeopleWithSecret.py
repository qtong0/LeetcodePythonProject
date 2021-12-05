from typing import List


class Solution:
    # Union Find
    # TC: O(M*Log(M) + (M+N)*Log(N)) where M is the length of Meeting
    # SC: O(M+N)
    #
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        roots = list(range(n))
        roots[firstPerson] = 0
        meetings.sort(key=lambda x: x[2])
        i = 0
        m = len(meetings)
        while i < m:
            people = []
            time = meetings[i][2]
            while i < m and time == meetings[i][2]:
                p1, p2 = meetings[i][0], meetings[i][1]
                root1 = self.find(roots, p1)
                root2 = self.find(roots, p2)
                roots[root1] = root2
                people.append(p1)
                people.append(p2)
                i += 1
            # if this person doesn't have a secret, reset it
            for p in people:
                if self.find(roots, p) != self.find(roots, 0):
                    roots[p] = p
        res = []
        for p in range(n):
            if self.find(roots, p) == self.find(roots, 0):
                res.append(p)
        return res

    def find(self, roots, node):
        while node != roots[node]:
            node = roots[node]
        return node



    def test(self):
        test_cases = [
            [6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1],
            [4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3],
            [5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1],
            [5, [[1,4,3], [0,4,3]], 3],
        ]
        for n, meetings, firstPerson in test_cases:
            res = self.findAllPeople(n, meetings, firstPerson)
            print('res: %s' % res)
            print('-=' * 30 + '-')



if __name__ == '__main__':
    Solution().test()
