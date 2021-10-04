from typing import List


class Solution:
    # Had to sort it first, otherwise won't pass test cases like this:
    # [4,4,16,20,8,8,2,10]
    #
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        hashmap = {}
        for num in changed:
            hashmap[num] = hashmap.get(num, 0) + 1
        res = []
        for num in changed:
            if num*2 in hashmap and num in hashmap:
                res.append(num)
                hashmap[num*2] -= 1
                if hashmap[num*2] == 0:
                    del hashmap[num*2]
                if num not in hashmap:
                    return []
                hashmap[num] -= 1
                if hashmap[num] == 0:
                    del hashmap[num]
        return res if not hashmap else []

    def test(self):
        test_cases = [
            [1,3,4,2,6,8],
            [6,3,0,1],
            [1],
            [4,4,16,20,8,8,2,10],
        ]
        for changed in test_cases:
            res = self.findOriginalArray(changed)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
