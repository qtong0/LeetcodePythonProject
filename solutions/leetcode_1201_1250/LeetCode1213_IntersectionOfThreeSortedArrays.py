class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        res = []
        i, j, k = 0, 0, 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return res

    # own solution - should be also fine
    def arraysIntersection_own(self, arr1, arr2, arr3):
        tmp = self.helper(arr1, arr2)
        return self.helper(tmp, arr3)

    def helper(self, arr1, arr2):
        i, j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                res.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        return res

