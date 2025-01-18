""" In this file, the Random Walk module is going to be created. 
    1. The RandomWalk class will be created and it is going to make the random decisions about the direction the walk will take.
    2. The class will have three attributes:
        i. one-variable to store the number of points in the walk. 
        ii. two lists, x_values and y_values, which will store the values of the walk. 
    3. The class will have one method, fill_walk(), which will calculate the points in the walk.
    4. The fill_walk() method will continue to take steps until the walk reaches the desired length.
    5. The fill_walk() method will use the choice() function to make random decisions about the direction the walk will take."""
    

from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step