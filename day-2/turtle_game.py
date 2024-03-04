import turtle
import random, time

WIDTH, HEIGHT = 500, 900
COLORS = ["red", "green", "blue", "orange", "yellow", "pink", "purple", "brown", "black", "cyan"]

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if  y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]

def iinit_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Trutle Race!")
    racers = screen.textinput("Enter age", "AGE")
    random.shuffle(COLORS)
    colors = COLORS[:int(racers)]
    winner = race(colors)
    return winner

def create_turtles(colors):
    turtles = []
    spacex = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacex , (-HEIGHT // 2) + 50 )
        racer.pendown()
        turtles.append(racer)
    return turtles

winner =iinit_turtle()
print(f"Turtle with color {winner} has won the race!")