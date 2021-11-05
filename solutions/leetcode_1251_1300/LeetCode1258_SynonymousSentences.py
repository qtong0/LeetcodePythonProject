from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parents = {}
        for w1, w2 in synonyms:
            root1 = self.findRoot(parents, w1)
            root2 = self.findRoot(parents, w2)
            if root1 != root2:
                parents[root1] = root2
        hashmap = {}
        for w1, w2 in synonyms:
            root1 = self.findRoot(parents, w1)
            hashmap[root1] = hashmap.get(root1, []) + [w1, w2]

        arr = text.split(' ')
        res = set()
        self.dfs(parents, hashmap, arr, 0, res, [])
        return sorted(res)

    def dfs(self, parents, hashmap, arr, i, res, curr):
        if i == len(arr):
            res.add(' '.join(curr))
            return
        root = self.findRoot(parents, arr[i])
        for w in hashmap.get(root, [root]):
            self.dfs(parents, hashmap, arr, i+1, res, curr + [w])

    def findRoot(self, parents, w):
        while w in parents:
            w = parents[w]
        return w

    def test(self):
        test_cases = [
            [[["a","b"],["b","c"],["d","e"],["c","d"]], "a b"],
            [[["happy","joy"],["sad","sorrow"],["joy","cheerful"]], "I am happy today but was sad yesterday"],
            [[["happy","joy"],["cheerful","glad"]], "I am happy today but was sad yesterday"],
            [[["a","b"],["c","d"],["e","f"]], "a c e"],
            [[["a","QrbCl"]], "d QrbCl ya ya NjZQ"],
        ]
        for synonyms, text in test_cases:
            res = self.generateSentences(synonyms, text)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
