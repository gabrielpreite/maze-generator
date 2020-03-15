import numpy as np
import random
import time

def recursive(x, y):
    #print("x:"+str(x)+"y:"+str(y))
    print(visited)
    time.sleep(0.5)
    visited[x][y] = 1

    nb = []
    if(x>0 and not visited[x-1][y]):
        nb.append([x-1, y])
    if(y>0 and not visited[x][y-1]):
        nb.append([x, y-1])
    if(x<size_x-1 and not visited[x+1][y]):
        nb.append([x+1, y])
    if(y<size_y-1 and not visited[x][y+1]):
        nb.append([x, y+1]) #checks for neighbours
    
    while nb:
        sel = random.randint(-0, len(nb)-1)
        #print("xs:"+str(nb[sel][0])+"ys:"+str(nb[sel][1]))
        if not visited[nb[sel][0]][nb[sel][1]]:
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
            xs = nb[sel][0]
            ys = nb[sel][1]
            visited[nb[sel][0]][nb[sel][1]] = 1 #mark as visited
        nb.remove([nb[sel][0], nb[sel][1]])
        for i in range(size_x):
            for j in range(size_y):
                print(maze[i][j], end=' ')
            print("\n")
        recursive(xs, ys)
    return

random.seed()
size_x = 5
size_y = 4

maze = [[[1 for i in range(4)] for j in range(size_y)] for k in range(size_x)]
visited = np.zeros([size_x, size_y])

recursive(0, 0)

for i in range(size_x):
    for j in range(size_y):
        print(maze[i][j], end=' ')
    print("\n")