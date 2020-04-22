class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        arr = [a, b, c]
        arr.sort()
        if arr[2] - arr[0] == 2:
            return [0, 0]
        if min(arr[1]-arr[0], arr[2]-arr[1] <= 2):
            minMoves = 1
        else:
            minMoves = 2
        return [minMoves, arr[2]-arr[0]-2]
