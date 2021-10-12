class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.arr = [[0, big], [0, medium], [0, small]]

    def addCar(self, carType: int) -> bool:
        if carType > 3 or carType <= 0:
            return False
        if self.arr[carType-1][0] == self.arr[carType-1][1]:
            return False
        self.arr[carType-1][0] += 1
        return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

obj = ParkingSystem(1,1,0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
