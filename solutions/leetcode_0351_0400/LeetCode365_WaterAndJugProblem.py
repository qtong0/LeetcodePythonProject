class Solution(object):
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == targetCapacity or jug2Capacity == targetCapacity or jug1Capacity+jug2Capacity == targetCapacity:
            return True
        while jug2Capacity != 0:
            tmp = jug2Capacity
            jug2Capacity = jug1Capacity%jug2Capacity
            jug1Capacity = tmp
        return bool(targetCapacity % jug1Capacity == 0)
