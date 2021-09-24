class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        stack = []
        n = len(cars)
        res = [-1]*n
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0] - p) / (s-cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        return res

    # Own solution, but TLE :(
    def getCollisionTimes_own_TLE(self, cars: list[list[int]]) -> list[float]:
        collide = True
        n = len(cars)
        res = [-1]*n
        prev_time = 0
        while collide:
            collide = False
            next_cars = []
            next_time = float('inf')
            next_ind = -1
            for i in range(n-1):
                if cars[i][1] > cars[i+1][1]:
                    collide_time = (cars[i+1][0]-cars[i][0]) / float(cars[i][1] - cars[i+1][1])
                    if collide_time < next_time:
                        next_time = collide_time
                        next_ind = i
                        collide = True
            if next_time != float('inf'):
                if res[next_ind] == -1:
                    res[next_ind] = prev_time + next_time
                prev_time += next_time
                for i in range(n):
                    if i == next_ind:
                        speed = cars[i+1][1]
                        pos = cars[i][0] + cars[i][1] * next_time
                        next_cars.append([pos, speed])
                        next_cars.append([pos, speed])
                    elif i-1 == next_ind:
                        continue
                    else:
                        speed, pos = cars[i][1], cars[i][0]+cars[i][1]*next_time
                        next_cars.append([pos, speed])
            cars = next_cars
        return res

    def test(self):
        test_cases = [
            # [[1,2],[2,1],[4,3],[7,2]],
            [[3,4],[5,4],[6,3],[9,1]],
        ]
        for cars in test_cases:
            res = self.getCollisionTimes(cars)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
