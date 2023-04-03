import tkinter as tk
import random

root = tk.Tk()
root.title("Pac man game")
root.geometry("600x680")
canvas = tk.Canvas(root)

grid= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 3, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 3, 0, 1, 1, 2, 1, 1, 0, 1, 0, 0, 3, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 4, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 1, 0],
    [0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
win = False
end = False
score = 0
moving = []

def arrayToDrawing():
    global score
    for Y in range (len(grid)):
        for X in range  (len(grid[Y])):
            x1 = (X * 33)
            x2 = 33 + x1
            y1 = (Y * 33)
            y2 = 33 + y1
            if  grid[Y][X] == 1:
                canvas.create_image(x1+35, y1+35, image = coins) 
            elif grid[Y][X] == 2:
                canvas.create_image(x1+35, y1+35, image = playeR)
            elif grid[Y][X] == 3:
                canvas.create_image(x1+35, y1+35, image = zombies)
            elif  grid[Y][X] == 4:
                canvas.create_rectangle(x1,y1,x2,y2, fill = "", outline = "")
            else:
                canvas.create_image(x1+35, y1+35, image = walls)

    canvas.create_text(300,665, text = "Score: "+str(score),font=("Comic Sans", 20))

def player(grid):
    for index1 in range(len(grid)):
        for index2 in range (len(grid[index1])):
            if grid[index1][index2] == 2:
                position = [index1, index2]

    return position

def endGame():
    global grid 
    grid = []
    arrayToDrawing()
 
def show_score():
    global score,end
    myScore = "Score: "+str(score)
    if end:
        canvas.delete('all')
        if score != 153:
            canvas.create_image(310, 335, image = endgame)
            canvas.create_text(325,400, text = "Your"+" "+myScore, font=("Comic Sans", 25))
        else:
            canvas.create_image(320, 260, image = playWin)
            canvas.create_image(310,500, image = youWin)

def indexOfenemy(grid):
    indexEnemy = []
    for index in range (len(grid)):
        for inline in range(len(grid[index])):
            if grid[index][inline] == 3:
                indexEnemy.append([index, inline])
    return indexEnemy

def canMove(grid, r, c):
    global moving
    moving = []
    if grid[r][c-1] != 0 and grid[r][c-1] != 3:
        moving.append("left")
    if grid[r][c]+1 != 0 and grid[r][c+1] != 3:
        moving.append("right")
    if grid[r-1][c] != 0  and grid[r-1][c] != 3:
        moving.append("up")
    if grid[r+1][c] != 0 and grid[r+1][c] != 3:
        moving.append("down")
    return moving

def enemyMove():
    global grid, moving, end
    enemyIndex = indexOfenemy(grid)
    for enemy in enemyIndex:
        rIndex = enemy[0]
        cIndex = enemy[1]
        whereToMove = canMove(grid, rIndex, cIndex)
        if len(whereToMove) > 0:
            moving = random.choice(whereToMove)
            if moving =="right":
                if grid[rIndex+1][cIndex] == 2:
                    end = True
                elif grid[rIndex][cIndex+1] !=2 and grid[rIndex][cIndex+1] == 4:
                    grid[rIndex][cIndex+1] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex][cIndex+1] != 2 and grid[rIndex][cIndex+1] == 1:
                    grid[rIndex][cIndex+1] = 3
                    grid[rIndex][cIndex] = 1
            if moving =="left":
                if grid[rIndex-1][cIndex] == 2:
                    end = True
                elif grid[rIndex][cIndex-1] != 2 and grid[rIndex][cIndex-1] == 4:  
                    grid[rIndex][cIndex-1] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex][cIndex-1] != 2 and grid[rIndex][cIndex-1] == 1:
                    grid[rIndex][cIndex-1] = 3
                    grid[rIndex][cIndex] = 1
            if moving =="up":
                if grid[rIndex-1][cIndex] == 2:
                    end = True
                elif grid[rIndex-1][cIndex] !=  2 and grid[rIndex-1][cIndex] == 4:
                    grid[rIndex-1][cIndex] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex-1][cIndex] != 2 and grid[rIndex-1][cIndex] == 1:
                    grid[rIndex-1][cIndex] = 3
                    grid[rIndex][cIndex] = 1
            if moving =="down":
                if grid[rIndex+1][cIndex] == 2:
                    end = True
                elif grid[rIndex+1][cIndex] != 2 and grid[rIndex+1][cIndex] == 4:
                    grid[rIndex+1][cIndex] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex+1][cIndex] != 2 and grid[rIndex+1][cIndex] == 1:
                    grid[rIndex+1][cIndex] = 3
                    grid[rIndex][cIndex] = 1
    canvas.delete("all")
    arrayToDrawing()
    canvas.after(400,enemyMove)
    if end:
        endGame()
        show_score()
        
def moveRight(event):
    global grid, score, end,  win
    if not end:
        position = player(grid)
        positionY = position[0]
        positionX = position[1]
        if grid[positionY][positionX+1] != 0 and positionX < len(grid)-1:
            grid[positionY][positionX] = 4
            if grid[positionY][positionX+1] == 1:
                score += 1
            if grid[positionY][positionX+1] == 3:
                end = True
                endGame()
            if not end:
                grid[positionY][positionX+1] = 2
            if score == 153:
                end = True
                endGame()
        
    canvas.delete("all")
    arrayToDrawing()
    show_score()
    
def moveLeft(event):
    global grid, score, end, win
    if not end:
        position = player(grid)
        positionY = position[0]
        positionX = position[1]
        if grid[positionY][positionX-1] != 0 and positionX > 0:
            grid[positionY][positionX] = 4
            if grid[positionY][positionX-1] == 1:
                score += 1
            if grid[positionY][positionX-1] == 3:
                end = True
                endGame()
            if not end:
                grid[positionY][positionX-1] = 2
            if score == 153:
                end = True
                endGame()

    canvas.delete("all")
    arrayToDrawing()
    show_score()

def moveUp(event):
    global grid, score, end, win
    if not end:
        position = player(grid)
        positionY = position[0]
        positionX = position[1]
        if grid[positionY-1][positionX] != 0 and positionY > 0:
            grid[positionY][positionX] = 4
            if grid[positionY-1][positionX] == 1:
                score += 1
            if grid[positionY-1][positionX] == 3:
                end = True
                endGame()
            if not end:
                grid[positionY-1][positionX] = 2
            if score == 153:
                end = True
                endGame()

    canvas.delete("all")
    arrayToDrawing()
    show_score()

def moveDown(event):
    global grid, score, end, win
    if not end:
        position = player(grid)
        positionY= position[0]
        positionX = position[1]
        if grid[positionY+1][positionX] != 0 and positionY < len(grid)-1:
            grid[positionY][positionX] = 4
            if grid[positionY+1][positionX] == 1:
                score += 1
            if grid[positionY+1][positionX] == 3:
                end = True
                endGame()
            if not end:
                grid[positionY+1][positionX] = 2
            if score == 153:
                end = True
                endGame()

    canvas.delete("all")
    arrayToDrawing()
    show_score()

playeR = tk.PhotoImage( file="./images/maleAdventurer_walk1.png")
zombies = tk.PhotoImage( file="./images/zombies.png")
coins = tk.PhotoImage( file ="./images/coinGold.png")
walls = tk.PhotoImage( file ="./images/images.png")
endgame = tk.PhotoImage( file ="./images/gameover.png")
youWin = tk.PhotoImage( file ="./images/congrats.png")
playWin = tk.PhotoImage( file ="./images/win.png")

root.bind("<Left>", moveLeft) #LEFT
root.bind("<Right>", moveRight) #RIGHT 
root.bind("<Up>", moveUp) #Up
root.bind("<Down>", moveDown) #Down

enemyMove()
arrayToDrawing()
canvas.pack(expand=True, fill="both")
root.mainloop()