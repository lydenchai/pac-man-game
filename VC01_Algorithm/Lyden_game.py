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
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 3, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 3, 0, 1, 0, 1, 0, 4, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
score = 0
#-----------------------------FUNCTION-----------------------------
def arrayToDrawing():
    global score
    myScore = 'SCORE:'+str(score)
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
                # canvas.create_rectangle(x1,y1,x2,y2, fill = "blue", outline = "")
                canvas.create_image(x1+20, y1+20, image = walls)
    canvas.create_text(425,980, text = myScore, font=("Comic Sans", 25))
def player(grid):
    for index1 in range(len(grid)):
        for index2 in range (len(grid[index1])):
            if grid[index1][index2] == 2:
                position = [index1, index2]
    return position
#-----------------------------MONSTER MOVE-----------------------------

#-----------------------------PLAYER MOVE-----------------------------
def moveRight(event):
    global grid, score
    position = player(grid)
    positionY = position[0]
    positionX = position[1]
    if grid[positionY][positionX+1] == 1:
        score += 1
    if grid[positionY][positionX+1] == 3:
        print("Game over!!!")
    if grid[positionY][positionX+1] != 0 and positionX < len(grid)-1:
        grid[positionY][positionX] = 4
        grid[positionY][positionX+1] = 2
    
    canvas.delete("all")
    arrayToDrawing()
def moveLeft(event):
    global grid, score
    position = player(grid)
    positionY = position[0]
    positionX = position[1]
    if grid[positionY][positionX-1] == 1:
        score += 1
    if grid[positionY][positionX-1] == 3:
        print("Game over!!!")
    if grid[positionY][positionX-1] != 0 and positionX > 0:
        grid[positionY][positionX] = 4
        grid[positionY][positionX-1] = 2
    canvas.delete("all")
    arrayToDrawing()

def moveUp(event):
    global grid, score
    position = player(grid)
    positionY = position[0]
    positionX = position[1]
    if grid[positionY-1][positionX] == 1:
        score += 1
    if grid[positionY-1][positionX] == 3:
        print("Game over!!!")
    if grid[positionY-1][positionX] != 0 and positionY > 0:
        grid[positionY][positionX] = 4
        grid[positionY-1][positionX] = 2
    canvas.delete("all")
    arrayToDrawing()

def moveDown(event):
    global grid, score
    position = player(grid)
    positionY= position[0]
    positionX = position[1]
    if grid[positionY+1][positionX] == 1:
        score += 1
    if grid[positionY+1][positionX] == 3:
        print("Game over!!!")
    if grid[positionY+1][positionX] != 0 and positionY < len(grid)-1:
        grid[positionY][positionX] = 4
        grid[positionY+1][positionX] = 2
    canvas.delete("all")
    arrayToDrawing()

#-----------------------------START GAME-----------------------------



#-----------------------------UPDATE SCORE-----------------------------
playeR = tk.PhotoImage( file="maleAdventurer_walk1.png" )
zombies = tk.PhotoImage( file="zombies.png" )
coins = tk.PhotoImage( file = "coinGold.png" )
walls = tk.PhotoImage( file = "bestwall.png" )

root.bind("<Left>", moveLeft) #LEFT CLICK
root.bind("<Right>", moveRight)  #RIGHT CLICK
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)  #Down CLICK

arrayToDrawing()
canvas.pack(expand=True, fill="both")
root.mainloop()