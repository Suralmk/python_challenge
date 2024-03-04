"""
    Maze Runner Game
"""
import sys, os
WALL = "#"
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9618)
def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end="")
            elif (x, y) == (exitx, exity):
                print(EXIT, end="")
            elif maze[(x, y)] == WALL:
                print(BLOCK, end="")
            else:
                print(maze[(x, y)], end="")
                
        print()

# THE GAME STARTS HERE      
while True:
    print("""Enter the name of the meze file (.txt) 
          to generate the maze runner game.
           Enter 'q' to quit! """)
    file = input(">  ")
    if file.upper() != "Q":
        print("Maze files  found are: \n")
        for f in os.listdir():
            if f.startswith("maze") and f.endswith(".txt"):
                print(" ", f)

    if file.upper() == "Q":
        sys.exit()

    if os.path.exists(file):
        break
    print("There is no file named {}".format(file))  

mazefile = open(file)
maze = {}
lines = mazefile.readlines()
playerx = None
playery = None
exitx = None
exity = None

y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, charachter in enumerate(line.rstrip()):
        assert charachter in (WALL, EMPTY, START, EXIT), "Invalid charachter at column {}, line {}".format(x + 1, y + 1 )
        if charachter in (WALL, EMPTY):
            maze[(x, y)] = charachter
        elif charachter == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif charachter == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1

HEIGHT = y
assert playerx != None and playery != None, "No start in maze file"
assert exitx != None and exity != None, "No exit in maze file"

while True:
    displayMaze(maze)
    while True: # Getting user move
        print("                        W      ")
        print("Enter Direction      A  S  D   ")

        move = input("> ")
        if move.upper() == "Q":
            print("Thanks for palying!")
            sys.exit()
        if move.upper() not in ["W", "A", "S", "D"]:
            print("Please  enter a valid move!")
            continue

        # Check if the player can move in the 'move' direction
        if move.upper() == "W" and maze[(playerx, playery - 1)] == EMPTY:
            print("You cant move upwards!")
            break
        elif move.upper() == "S" and maze[(playerx, playery + 1)] == EMPTY:
            print("You cant move Downwards!")
            break
        elif move.upper() == "A" and maze[(playerx - 1, playery)] == EMPTY:
            print("You cant move to Left!")
            break
        elif move.upper() == "D" and maze[(playerx + 1, playery)] == EMPTY:
            print("You cant move to Right!")
            break

    # Keep moving in the 'move' direction untill you reach a block
    if move.upper() == "W":
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break #Break if player reach exit point
            if maze[(playerx, playery - 1)] == WALL:
                break # break if player reaches a wall
            if (playerx - 1, playery) == EMPTY or (playerx + 1, playery) == EMPTY:
                break #  Breake if player have reached branch point


    elif move.upper() == "S":
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break #Break if player reach exit point
            if maze[(playerx, playery + 1)] == WALL:
                break # break if player reaches a wall
            if (playerx - 1, playery) == EMPTY or (playerx + 1, playery) == EMPTY:
                break #  Breake if player have reached branch point

    elif move.upper() == "A":
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break #Break if player reach exit point
            if maze[(playerx - 1, playery)] == WALL:
                break # break if player reaches a wall
            if (playerx , playery - 1) == EMPTY or (playerx , playery + 1) == EMPTY:
                break #  Breake if player have reached branch point

    elif move.upper() == "D":
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break #Break if player reach exit point
            if maze[(playerx + 1, playery)] == WALL:
                break # break if player reaches a wall
            if (playerx , playery - 1) == EMPTY or (playerx , playery + 1) == EMPTY:
                break #  Breake if player have reached branch point

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print("You have reached the exit! Great JOB")
        sys.exit()