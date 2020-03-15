import numpy as np
import random

size_x = 5
size_y = 4

maze_mask = [[[0 for i in range(4)] for j in range(size_y)] for k in range(size_x)]
random.seed()

for i in range(size_x): #generates random map
    for j in range(size_y):
        print(str(i)+", "+str(j))
        maze_mask[i][j] = [-1, -1, -1, -1]
        if(i>0): #up
            maze_mask[i][j][0] = random.randint(1, 100)
        if(j>0): #left
            maze_mask[i][j][1] = random.randint(1, 100)
        if(i<size_x-1): #down
            maze_mask[i][j][2] = random.randint(1, 100)
        if(j<size_y-1): #right
            maze_mask[i][j][3] = random.randint(1, 100)
#maze_mask[0][0][1] = 0
#maze_mask[size_x-1][size_y-1][3] = 0 #opens entrance and exit

for i in range(size_x):
    for j in range(size_y):
        print(maze_mask[i][j], end=' ')
    print("\n")

edges = list()

for i in range(size_x):
    for j in range(size_y):
        for k in range(4):
            if(maze_mask[i][j][k]>0):
                edges.append([maze_mask[i][j][k], i, j])
edges.sort() #creates a graph from the mask
for i in edges:
    print(i)

"""for i in range(size_x):
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
    print("\n")"""