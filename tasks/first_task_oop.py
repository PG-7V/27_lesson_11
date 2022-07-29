import random
import time

class PlayingCube:

    def __init__(self, num):
        self.num = num

    def roll(self):
        return random.randint(1, self.num)




cub_1 = PlayingCube(6)

for i in range(10):
    print(cub_1.roll())
    time.sleep(1)



























