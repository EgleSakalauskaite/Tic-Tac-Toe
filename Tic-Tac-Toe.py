from random import randint
grid = [" "] * 9

def get_board():
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(grid[0], grid[1], grid[2], grid[3], grid[4], grid[5], grid[6], grid[7], grid[8]))

def player(shape):
    shape_pos = int(input("Where do you want to place your "+shape+"? (1-9) "))
    if shape_pos < 1 or shape_pos > 9:
        print("You can only choose numbers between 1 to 9")
    else:
        if grid[shape_pos-1] != " ":
            print("This square is already taken, pick another one ")
            player(shape)
        else:
            grid[shape_pos-1] = shape
            get_board()

def robot():
    shape_pos = randint(1, 9)
    if grid[shape_pos-1] != " ":
        robot()
    else:
        grid[shape_pos-1] = "O"
        get_board()

def win_check(xo):
    if xo == "X":
        match = "XXX"
    else:
        match = "OOO"
    r1 = grid[0] + grid[1] + grid[2]
    r2 = grid[3] + grid[4] + grid[5]
    r3 = grid[6] + grid[7] + grid[8]
    c1 = grid[0] + grid[3] + grid[6]
    c2 = grid[1] + grid[4] + grid[7]
    c3 = grid[2] + grid[5] + grid[8]
    d1 = grid[0] + grid[4] + grid[8]
    d2 = grid[2] + grid[4] + grid[6]
    if r1==match or r2==match or r3==match or c1==match or c2==match or c3==match or d1==match or d2==match:
        return True
    else:
        return False

mode = input("Do you wish to challenge a friend or a robot?")
print("1|2|3\n4|5|6\n7|8|9")

while 1 == 1:
    player("X")
    if win_check("X") == True:
        print("Player X wins")
        break
    elif mode == "friend":
        player("O")
        if win_check("O") == True:
            print("Player O wins")
            break
    else:
        robot()
        if win_check("O") == True:
            print("Robot wins")
            break
