import tkinter as tk
import random
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH=TILE_SIZE*COLS   #25X25=625
WINDOW_HEIGHT=TILE_SIZE*ROWS  #25X25=625

class Tile:
    def _init_(self,x,y):
        self.x=x
        self.y=y

window=tk.Tk()
window.title("Snake Game")
window.geometry(f"{WINDOW_HEIGHT}x{WINDOW_WIDTH}")
window.resizable(False,False)

canvas=tk.Canvas(window,bg="black",width=WINDOW_WIDTH,height=WINDOW_HEIGHT,borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()

# window_width=window.winfo_width()
# window_height=window.winfo_height()

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=(screen_width//2) - (WINDOW_WIDTH//2)
window_y=(screen_height//2) - (WINDOW_HEIGHT//2)

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")

#Initializing the snake
snake=Tile(5*TILE_SIZE,5*TILE_SIZE) #initial position of the snake
food=Tile(20*TILE_SIZE,20*TILE_SIZE) #initial position of the food
velocityX=0
velocityY=0
snake_body=[]  #initialize snake body as empty list
game_over=False
score=0

def change_direction(e):
    # print(e)
    #print(e.keysym)
    global velocityY,velocityX
    if(e.keysym == "Up" and velocityY!=1):
        velocityX=0
        velocityY=-1
    elif(e.keysym == "Down" and velocityY!=-1): 
        velocityX=0
        velocityY=1
    elif(e.keysym == "Right" and velocityX!=-1):
        velocityX=1
        velocityY=0
    elif(e.keysym == "Left" and velocityX!=1):
        velocityX=-1
        velocityY=0
        
def move():
    global snake,food,game_over,score
    
    if (game_over):
        return
    if (snake.x<0 or snake.x>=WINDOW_WIDTH or snake.y<0 or snake.y>=WINDOW_HEIGHT):
        game_over=True
        return
    for tile in snake_body:
        if(snake.x==tile.x and snake.y==tile.y):
            game_over=True
            return
    
   
    if(snake.x == food.x and snake.y == food.y):
        score+=1
        snake_body.append(Tile(food.x,food.y))
        food.x=random.randint(0,COLS-1)*TILE_SIZE
        food.y=random.randint(0,ROWS-1)*TILE_SIZE
    #Update the snake body
    for i in range(len(snake_body)-1,-1,-1):
        tile=snake_body[i]
        if(i==0):
            tile.x=snake.x
            tile.y=snake.y
        else :
            prev_tile=snake_body[i-1]
            tile.x=prev_tile.x
            tile.y=prev_tile.y        
    
    snake.x+=velocityX*TILE_SIZE
    snake.y+=velocityY*TILE_SIZE    
        
    
def draw():
    global snake,food
    move()
    
    canvas.delete("all")
    #draw snake and food
    canvas.create_oval(food.x,food.y,food.x+TILE_SIZE,food.y+TILE_SIZE,fill='red')
    canvas.create_rectangle(snake.x,snake.y,snake.x+TILE_SIZE,snake.y+TILE_SIZE,fill='green')
    for i in snake_body:
            canvas.create_rectangle(i.x,i.y,i.x+TILE_SIZE,i.y+TILE_SIZE,fill='green')
    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,font="Arial 20",text=f"Game Over : {score}",fill="white")
    else :
        canvas.create_text(30,20,font="Arial 10",text=f"Score: {score}",fill="white")                    
    window.after(175,draw)

draw()
    
window.bind("<KeyRelease>",change_direction) 

window.mainloop()