class Solution(object):
    def numFriendRequests(self, ages) -> int:
        hashmap = {}
        for age in ages:
            hashmap[age] = hashmap.get(age, 0)+1
        res = 0
        for age1 in hashmap.keys():
            for age2 in hashmap.keys():
                if self.request(age1, age2):
                    if age1 == age2:
                        res += hashmap[age1] * (hashmap[age2]-1)
                    else:
                        res += hashmap[age1] * hashmap[age2]
        return res

    def request(self, age1, age2):
        return not (age2 <= 0.5*age1+7 or age2 > age1 or (age2 > 100 and age1 < 100))
    
    def test(self):
        testCases = [
            [16,16],
            [16,17,18],
            [20,30,100,110,120],
            [54,23,102,90,40,74,112,74,76,21],
        ]
        for ages in testCases:
            print('ages: %s' % ages)
            result = self.numFriendRequests(ages)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
