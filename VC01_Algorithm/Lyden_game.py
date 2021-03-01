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
win = False
score = 0
end = False

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
    canvas.create_text(425,970, text = "Score: "+str(score), font=("Comic Sans", 25))

def player(grid):
    for index1 in range(len(grid)):
        for index2 in range (len(grid[index1])):
            if grid[index1][index2] == 2:
                position = [index1, index2]
    return position
#-----------------------------START GAME-----------------------------

#-----------------------------END GAME-----------------------------
def endGame():
    global grid 
    grid = []
    arrayToDrawing()

def show_score():
    global score,end
    myScore = 'Score:'+str(score)
    if end:
        canvas.delete('all')
        gameOver = canvas.create_image(420, 320, image = endgame)
        canvas.create_text(410,440, text = "Your"+" "+myScore, font=("Comic Sans", 25))

#-----------------------------PLAYER WIN-----------------------------
def playerWin():
    global score 
    if score == 159 and not end:
        canvas.delete("all")
        gameWin = canvas.create_image(425, 320, image = youWin)
        canvas.create_text(440,470, text = "You Win!", font=("Comic Sans", 50))

#-----------------------------MONSTER MOVE-----------------------------

#-----------------------------PLAYER MOVE-----------------------------
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
                end = False
            if grid[positionY][positionX+1] == 3:
                end = True
                endGame()
            if not end:
                grid[positionY][positionX+1] = 2
        
    canvas.delete("all")
    arrayToDrawing()
    show_score()
    playerWin()
    
def moveLeft(event):
    global grid, score, end
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

    canvas.delete("all")
    arrayToDrawing()
    show_score()
    playerWin()

def moveUp(event):
    global grid, score, end
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

    canvas.delete("all")
    arrayToDrawing()
    show_score()
    playerWin()

def moveDown(event):
    global grid, score, end
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

    canvas.delete("all")
    arrayToDrawing()
    show_score()
    playerWin()
#-----------------------------IMAGE-----------------------------
playeR = tk.PhotoImage( file="maleAdventurer_walk1.png" )
zombies = tk.PhotoImage( file="zombies.png" )
coins = tk.PhotoImage( file = "coinGold.png" )
walls = tk.PhotoImage( file = "bestwall.png" )
endgame = tk.PhotoImage( file = "gameover.png" )
youWin = tk.PhotoImage( file = "con.png" )

root.bind("<Left>", moveLeft) #LEFT CLICK
root.bind("<Right>", moveRight)  #RIGHT CLICK
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)  #Down CLICK

arrayToDrawing()
canvas.pack(expand=True, fill="both")
root.mainloop()