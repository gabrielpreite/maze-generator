import numpy as np
import random

size_x = 5
size_y = 5

map = np.zeros((size_x, size_y))
random.seed()

for i in range(size_x): #generates random map
    for j in range(size_y):
        map[i][j] = random.randint(0, 3)

for i in range(size_x):
    for j in range(size_y):
        print(int(map[i][j]), end=' ')
    print("\n")

maze_mask = [[[0 for i in range(4)] for j in range(size_x)] for k in range(size_y)]

for i in range(size_x):
    for j in range(size_y):
        minim = 6
        mask = list("0000")
        if(i>0):
            minim = min(minim, map[i-1][j])
        if(j>0):
            minim = min(minim, map[i][j-1])
        if(i<size_x-1):
            minim = min(minim, map[i+1][j])
        if(j<size_y-1):
            minim = min(minim, map[i][j+1]) #finds the minimum value

        if(i>0 and map[i-1][j]==minim):
            mask[0] = "1"
        if(j>0 and map[i][j-1]==minim):
            mask[1] = "1"
        if(i<size_x-1 and map[i+1][j]==minim):
            mask[2] = "1"
        if(j<size_y-1 and map[i][j+1]==minim):
            mask[0] = "1" #connects the maze
        
        maze_mask[i][j] = mask

for i in range(size_x):
    for j in range(size_y):
        print(maze_mask[i][j], end=' ')
    print("\n")