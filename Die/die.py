""" Creating pygal class
This is the class that will simulate the rolling of a die
"""
from random import randint

class Die():
    
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)
    
    '''
    1. The _init function takes one optional argument. Since the the instance created 
        the number of sides will always be six so far no other argument is included.
    2. The roll method will uses the randint() function to return a random number integer 
        between 1 to the number of sides. It can return the starting value 1 and ending  value (num_sides)
    '''