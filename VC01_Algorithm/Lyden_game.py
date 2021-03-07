#-----------------------------IMPORTS-----------------------------
import tkinter as tk
import random

#-----------------------------CONSTANTS-----------------------------
root = tk.Tk()
root.title("Lyden_VC01_Game")
root.geometry("850x1000")
canvas = tk.Canvas(root)

#-----------------------------VARIABLES-----------------------------
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
tomove = []

                #----------NOTE---------#
                #       0 = walls       #
                #       1 = coin        #
                #       2 = player      #
                #       3 = zombies     #
                #       4 = space       #
                #-----------------------#

#-----------------------------FUNCTION-----------------------------
def arrayToDrawing():
    global score
    for Y in range (len(grid)):
        for X in range  (len(grid[Y])):
            x1 = (X * 50)
            x2 = 50 + x1
            y1 = (Y * 50)
            y2 = 50 + y1
            if  grid[Y][X] == 1:
                coin = canvas.create_image(x1+20, y1+20, image = coins) 
            elif grid[Y][X] == 2:
                player = canvas.create_image(x1+20, y1+20, image = playeR)
            elif grid[Y][X] == 3:
                monster = canvas.create_image(x1+20, y1+20, image = zombies)
            elif  grid[Y][X] == 4:
                canvas.create_rectangle(x1,y1,x2,y2, fill = "", outline = "")
            else:
                canvas.create_image(x1+20, y1+20, image = walls)

    canvas.create_text(425,970, text = "Score: "+str(score),font=("Comic Sans", 25))

def player(grid):
    for index1 in range(len(grid)):
        for index2 in range (len(grid[index1])):
            if grid[index1][index2] == 2:
                position = [index1, index2]

    return position

#-----------------------------END GAME-----------------------------
def endGame():
    global grid 
    grid = []
    arrayToDrawing()
 
#-----------------------------PLAYER WIN AND LOSE-----------------------------
def show_score():
    global score,end
    myScore = "Score: "+str(score)
    if end:
        canvas.delete('all')
        if score != 153:
            gameOver = canvas.create_image(420, 320, image = endgame)
            canvas.create_text(410,440, text = "Your"+" "+myScore, font=("Comic Sans", 25))
        else:
            gameWin = canvas.create_image(435, 320, image = playWin)
            p_w = canvas.create_image(450,740, image = youWin)
        
#-----------------------------MONSTER MOVE-----------------------------
def indexOfenemy(grid):
    indexEnemy = []
    for index in range (len(grid)):
        for inline in range(len(grid[index])):
            if grid[index][inline] == 3:
                indexEnemy.append([index, inline])
    return indexEnemy

def canMove(grid, r, c):
    global tomove
    tomove = []
    if grid[r][c-1] != 0 and grid[r][c-1] != 3:
        tomove.append("left")
    if grid[r][c]+1 != 0 and grid[r][c+1] != 3:
        tomove.append("right")
    if grid[r-1][c] != 0  and grid[r-1][c] != 3:
        tomove.append("up")
    if grid[r+1][c] != 0 and grid[r+1][c] != 3:
        tomove.append("down")
    return tomove

def enemyMove():
    global grid, tomove, end
    enemyIndex = indexOfenemy(grid)
    for enemy in enemyIndex:
        rIndex = enemy[0]
        cIndex = enemy[1]
        whereToMove = canMove(grid, rIndex, cIndex)
        if len(whereToMove) > 0:
            tomove = random.choice(whereToMove)
            if tomove =="right":
                if grid[rIndex+1][cIndex] == 2:
                    end = True
                elif grid[rIndex][cIndex+1] !=2 and grid[rIndex][cIndex+1] == 4:
                    grid[rIndex][cIndex+1] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex][cIndex+1] != 2 and grid[rIndex][cIndex+1] == 1:
                    grid[rIndex][cIndex+1] = 3
                    grid[rIndex][cIndex] = 1
            if tomove =="left":
                if grid[rIndex-1][cIndex] == 2:
                    end = True
                elif grid[rIndex][cIndex-1] != 2 and grid[rIndex][cIndex-1] == 4:  
                    grid[rIndex][cIndex-1] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex][cIndex-1] != 2 and grid[rIndex][cIndex-1] == 1:
                    grid[rIndex][cIndex-1] = 3
                    grid[rIndex][cIndex] = 1
            if tomove =="up":
                if grid[rIndex-1][cIndex] == 2:
                    end = True
                elif grid[rIndex-1][cIndex] !=  2 and grid[rIndex-1][cIndex] == 4:
                    grid[rIndex-1][cIndex] = 3
                    grid[rIndex][cIndex] = 4
                elif grid[rIndex-1][cIndex] != 2 and grid[rIndex-1][cIndex] == 1:
                    grid[rIndex-1][cIndex] = 3
                    grid[rIndex][cIndex] = 1
            if tomove =="down":
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
        
#----------------------------- PLAYER MOVE-----------------------------
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

#-----------------------------IMAGE-----------------------------
playeR = tk.PhotoImage( file="maleAdventurer_walk1.png" )
zombies = tk.PhotoImage( file="zombies.png" )
coins = tk.PhotoImage( file = "coinGold.png" )
walls = tk.PhotoImage( file = "images.png" )
endgame = tk.PhotoImage( file = "gameover.png" )
youWin = tk.PhotoImage( file = "congrats.png" )
playWin = tk.PhotoImage( file = "win.png")

root.bind("<Left>", moveLeft) #LEFT CLICK
root.bind("<Right>", moveRight)  #RIGHT CLICK
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)  #Down CLICK

enemyMove()
arrayToDrawing()
canvas.pack(expand=True, fill="both")
root.mainloop()