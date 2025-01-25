""" In this file, the Random Walk module is going to be created. 
    1. The RandomWalk class will be created and it is going to make the random decisions about the direction the walk will take.
    2. The class will have three attributes:
        i. one-variable to store the number of points in the walk. 
        ii. two lists, x_values and y_values, which will store the values of the walk. 
    3. The class will have one method, fill_walk(), which will calculate the points in the walk.
    4. The fill_walk() method will continue to take steps until the walk reaches the desired length.
    5. The fill_walk() method will use the choice() function to make random decisions about the direction the walk will take."""
    

from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        # All works start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
