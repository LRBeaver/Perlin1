__author__ = 'lyndsay.beaver'
import random
import math
newseed = random.randint(1,1000000000)
random.seed(newseed)

def generateWhiteNoise(width,height):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            noise[i][j] = random.randint(0,1)

    return noise

noise = generateWhiteNoise(50,12)

for i in noise:
    print()
    for o in i:
        if(o == 0):
            print('-',end='')
        else:
            print('#',end='')