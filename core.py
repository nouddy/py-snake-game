from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_PATTERN = "#737BE1"
FOOD_PATTERN = "#FF0000"
BACKGROUND_COLOR = "green"

class Snake:
    def __init__(self):
        self.bodySize = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y, in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_PATTERN, tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE)-1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)-1)) * SPACE_SIZE
 
        self.coordinate = [x, y]

        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_PATTERN, tags="food")

def nextTurn(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_PATTERN)

    snake.squares.insert(0, square)

    if x == food.coordinate[0]and y == food.coordinate[1]:

        global score
        score+=1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if collisionCheck(snake):
        end_game()

    else:

        window.after(SPEED, nextTurn, snake, food)

def changeDirection(new_direct):
    
    global direction

    if new_direct == 'left':
        if direction != 'right':
            direction = new_direct
    elif new_direct == 'right':
        if direction != 'left':
            direction = new_direct
    elif new_direct == 'up':
        if direction != 'down':
            direction = new_direct
    elif new_direct == 'down':
        if direction != 'up':
            direction = new_direct

def collisionCheck(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def end_game():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Arial', 60), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("SNAKE GAME")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('arial', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()