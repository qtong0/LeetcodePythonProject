from typing import List
from sortedcontainers import SortedDict


class Solution(object):
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = SortedDict()
        for num in hand:
            counter[num] = counter.get(num, 0) + 1
        queue = []
        opened, prev = 0, -1
        for num in counter:
            if (opened > 0 and num > prev + 1) or (opened > counter[num]):
                return False
            queue.append(counter[num] - opened)
            prev = num
            opened = counter.get(num)
            if len(queue) == groupSize:
                opened -= queue.pop(0)
        return opened == 0



    def isNStraightHand_own(self, hand, W):
        w = W
        if len(hand) % w != 0:
            return False
        hashmap = {}
        for num in hand:
            hashmap[num] = hashmap[num]+1 if num in hashmap else 1
        while hashmap:
            minVal = min(hashmap)
            for i in range(w):
                if minVal + i not in hashmap:
                    return False
                hashmap[minVal+i] -= 1
                if hashmap[minVal+i] == 0:
                    del hashmap[minVal+i]
        return len(hashmap) == 0
    
    def test(self):
        testCases = [
            [
                [1,2,3,6,2,3,4,7,8],
                3,
            ],
            [
                [1,2,3,4,5],
                4,
            ],
        ]
        for hand, w in testCases:
            result = self.isNStraightHand(hand, w)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
