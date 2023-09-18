import random
import time
import os

gridX = 50
gridY = 50
fullCell = "██"
emptyCell = "  "

def createGrid(x=gridX,y=gridY,fill="rand"):
    g = []
    for i in range(0,y):
        g.append([])
        for j in range (0,x):
            if fill == "rand":
                g[i].append(random.randint(0,1))
            elif fill == None:
                g[i].append(0)
    return g

def renderGrid(grid,k=0):
    renderedString = ''
    for y in range(0,len(grid)):
        columnString = ""
        for x in range(0,len(grid[y])):

            if k == 0: columnString += fullCell if grid[y][x] == 1 else emptyCell
            if k == 1: columnString += str(countNearbyCells(grid,y,x)) + "," if grid[y][x] == 1 else emptyCell
        renderedString += columnString + "\n"
    #os.system("cls")
    print("\033[H", end="")
    print(renderedString)

def countNearbyCells(grid,y,x):
    count = 0
    offsets = (-1,0,1)
    for i in offsets:
        for j in offsets:
            if not(i == 0 and j ==0):
                try:
                    if y+i >=0 and x+j >= 0:
                        if grid[y+i][x+j] == 1:
                            count += 1
                except IndexError:
                    pass
    return count

def updateGrid(grid):
    updatedGrid = createGrid(fill=None)
    for y in range(0,len(grid)):
        for x in range(0,len(grid[y])):
            count = countNearbyCells(grid,y,x)
            if count < 2 and grid[y][x] == 1:
                updatedGrid[y].append
            elif count > 3 and grid[y][x] == 1:
                updatedGrid[y][x] = 0
            elif count == 3 and grid[y][x] == 0:
                updatedGrid[y][x] = 1
            else:
                updatedGrid[y][x] = grid[y][x]
    return updatedGrid



grid = createGrid(fill="rand")

input()
while True:
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    renderGrid(grid)
    #renderGrid(grid,k=1)
    grid = updateGrid(grid)
    time.sleep(0.1)
    #if input() == "n": break