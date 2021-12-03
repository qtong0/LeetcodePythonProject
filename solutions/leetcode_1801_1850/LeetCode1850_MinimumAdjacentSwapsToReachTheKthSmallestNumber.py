class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        arr = list(num)
        for _ in range(k):
            self.nextPerm(arr)
        arr0 = list(num)
        return self.countSteps(arr0, arr)

    def countSteps(self, arr1, arr2):
        n = len(arr1)
        i, j = 0, 0
        count = 0
        while i < n:
            j = i
            while arr1[j] != arr2[i]:
                j += 1
            while i < j:
                arr1[j], arr1[j-1] = arr1[j-1], arr1[j]
                count += 1
                j -= 1
            i += 1
        return count

    def nextPerm(self, arr):
        n = len(arr)
        j = n-1
        while j > 0 and arr[j-1] >= arr[j]:
            j -= 1
        k = j-1
        i = k
        while i+1 < n and arr[i+1] > arr[k]:
            i += 1
        arr[i], arr[k] = arr[k], arr[i]
        j = n-1
        i = k+1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return 0


    def test(self):
        test_cases = [
            ["5489355142", 4],
            ["11112", 4],
            ["00123", 1],
            ["99499", 1],
        ]
        for nums, k in test_cases:
            res = self.getMinSwaps(nums, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
