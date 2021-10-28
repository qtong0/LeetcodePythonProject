from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            arr = [str(num) for num in arr]
            key = '|'.join(arr)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
    
    def test(self):
        test_cases = [
            ["eat","tea","tan","ate","nat","bat"],
            [''],
            ['a'],
            ["bdddddddddd","bbbbbbbbbbc"],
        ]
        for strs in test_cases:
            res =  self.groupAnagrams(strs)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
