import numpy as np
import random
import time
import cv2
import sys

random.seed()
size_x = int(sys.argv[1])
size_y = int(sys.argv[2])

maze = [[[1 for i in range(4)] for j in range(size_y)] for k in range(size_x)]
visited = np.zeros([size_x, size_y])

#recursive(0, 0)
stack = []
visited[0, 0] = 1
stack.insert(0, [0, 0])
while(stack):
    current = stack[0]
    stack.remove(current)
    nb = []
    x = current[0]
    y = current[1]
    #print("x:"+str(x)+"y:"+str(y))
    #time.sleep(0.5)
    if(x>0 and not visited[x-1][y]):
        nb.append([x-1, y])
    if(y>0 and not visited[x][y-1]):
        nb.append([x, y-1])
    if(x<size_x-1 and not visited[x+1][y]):
        nb.append([x+1, y])
    if(y<size_y-1 and not visited[x][y+1]):
        nb.append([x, y+1]) #checks for neighbours

    if nb:
        stack.insert(0, [x, y])
        sel = random.randint(0, len(nb)-1)
        if(nb[sel][0] == x-1 and nb[sel][1] == y):
            maze[x][y][0] = 0
            maze[x-1][y][2] = 0
        elif(nb[sel][0] == x and nb[sel][1] == y-1):
            maze[x][y][1] = 0
            maze[x][y-1][3] = 0
        elif(nb[sel][0] == x+1 and nb[sel][1] == y):
            maze[x][y][2] = 0
            maze[x+1][y][0] = 0
        elif(nb[sel][0] == x and nb[sel][1] == y+1):
            maze[x][y][3] = 0
            maze[x][y+1][1] = 0 #removes walls from current and selected node

        visited[nb[sel][0], nb[sel][1]] = 1
        stack.insert(0, [nb[sel][0], nb[sel][1]])
        """for i in range(size_x):
            for j in range(size_y):
                print(maze[i][j], end=' ')
            print("\n")"""

maze[0][0][1] = 0
maze[size_x-1][size_y-1][3] = 0 #removes walls at entrance and exit

for i in range(size_x):
    for j in range(size_y):
        print(maze[i][j], end=' ')
    print("\n")

image = np.zeros((size_x*3, size_y*3))

for i in range(size_x):
    for j in range(size_y):
        image[i*3+1][j*3+1] = 1 #removes wall at the center of each block

#cv2.imshow('image1', image)
#cv2.waitKey(0)

for i in range(size_x):
    for j in range(size_y):
        if(maze[i][j][0] == 0):
            image[i*3][j*3+1] = 1
        if(maze[i][j][1] == 0):
            image[i*3+1][j*3] = 1
        if(maze[i][j][2] == 0):
            image[i*3+2][j*3+1] = 1
        if(maze[i][j][3] == 0):
            image[i*3+1][j*3+2] = 1

cv2.imshow('image2', image)
cv2.waitKey(0)