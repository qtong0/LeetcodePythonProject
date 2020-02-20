# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       pass

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, (0, 0), 0, set())

    def dfs(self, robot, cell, d, visited):
        robot.clean()
        visited.add(cell)
        # going clockwise: 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = (-1, 0), (0, 1), (1, 0), (0, -1)
        for i in range(4):
            new_d = (d+i) % 4
            new_cell = (cell[0] + directions[new_d][0], \
                        cell[1] + directions[new_d][1])
            if new_cell not in visited and robot.move():
                self.dfs(robot, new_cell, new_d, visited)
                self.go_back(robot)
            robot.turnRight()

    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
