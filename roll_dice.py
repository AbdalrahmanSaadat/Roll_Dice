import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        result = (first,second)
        return result
        
        
rolling = Dice()
print(rolling.roll())