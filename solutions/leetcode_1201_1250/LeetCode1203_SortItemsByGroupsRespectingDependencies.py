from typing import List
import collections


class Solution:
    # Topological Sort
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # find the group of each item
        group2item = collections.defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group2item[group[i]].add(i)

        # find the relationships between the groups and each items in the same group
        t_pre, t_suc = collections.defaultdict(set), collections.defaultdict(set)
        g_pre, g_suc = collections.defaultdict(set), collections.defaultdict(set)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    t_pre[i].add(j)
                    t_suc[j].add(i)
                else:
                    g_pre[group[i]].add(group[j])
                    g_suc[group[j]].add(group[i])
        # topological sort the groups
        groups_order = self.topo_sort([i for i in group2item], g_pre, g_suc)
        # topological sort the items in each group
        t_order = []
        for i in groups_order:
            items = group2item[i]
            i_order = self.topo_sort(items, t_pre, t_suc)
            if len(i_order) != len(items):
                return []
            t_order += i_order
        return t_order if len(t_order) == n else []

    def topo_sort(self, points, pre, suc):
        order = []
        sources = [p for p in points if not pre[p]]
        while sources:
            s = sources.pop()
            order.append(s)
            for u in suc[s]:
                pre[u].remove(s)
                if not pre[u]:
                    sources.append(u)
        return order if len(order) == len(points) else []

    def test(self):
        test_cases = [
            [8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]],
            [8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]],
        ]
        for n, m, group, beforeItems in test_cases:
            res = self.sortItems(n, m, group, beforeItems)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
