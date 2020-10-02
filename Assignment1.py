import random

SHIP_SIZE = 4
DIMENSION = 10

#Create a board
board = [[0 for i in range(DIMENSION)] for x in range(DIMENSION)]


#randomly generate a ship
check = False
while check != True:
    ship = [random.randint(0,DIMENSION-1),random.randint(0,DIMENSION-1),random.randint(0,1)]
    #The number represents row_num,col_num,Direction respectively
    #0 stands for down, 1 stands for right

    #Make sure the randomly generated ship will be on board. If yes, add it on the board. If no, regenerate it
    if ship[2]==0:
        if ship[1]>=DIMENSION-(SHIP_SIZE-1):
            continue
        for x in range(SHIP_SIZE):
            board[ship[0]][ship[1]+x]=1
        check = True
    else:
        if ship[0]>=DIMENSION-(SHIP_SIZE-1):
            continue
        for x in range(SHIP_SIZE):
            board[ship[0]+x][ship[1]]=1
        check = True

#Game start:
print("Hello!Welcome to the Battleship game. Let's start!",end="\n"*2)
right_guess = 0
score = 0
while right_guess < SHIP_SIZE:
    #Display the board:

    #Row label:
    for row_label in range(65,65+DIMENSION):
        print("   "+chr(row_label),end="")
    print("\n")

    #col label and grid:
    for row in range(DIMENSION+1):
        #Print row line
        print(" "+"+---"*DIMENSION+"+",end="\n")

        #Make sure we won't have extra col_line(since col_line is one less than row_line
        if row==DIMENSION:
            break
        
        #Print col_label
        print(str(row),end="")

        #Print col_line
        for col in range(DIMENSION):
            if board[row][col] == 2:
                print("| # ",end="")
            elif board[row][col] == 3:
                print("| X ",end="")
            else:
                print("|   ",end="")

        #print the last "|" 
        print("|",end="\n")
            

    #Ask for input
    player_input = input("Enter coordinate to target(e.g. A1,B2): ")
    
    #Score count
    score = score + 1
    
    #Check whether the input is a capitalized letter followed by number
    if player_input[0].isalpha() == False:
        print("Wrong input!Your row guess should be a letter like:A. Input again!",end="\n"*2)
        continue
    elif player_input[0].isupper() == False:
        print("Wrong input!Your row guess should be a capitalized letter like:A. Input again!",end="\n"*2)
        continue
    elif player_input[1:].isdigit() == False:
        print("Wrong input!Your column guess should be a integer like:1. Input again!",end="\n"*2)
        continue

    #After making sure the input is the right format,convert it into row and col value
    col_guess = ord(player_input[0])-65
    row_guess = int(player_input[1:])

    #Check whether input is within the board and is not a repetitive guess
    if row_guess>=DIMENSION or row_guess<0 or col_guess<0 or col_guess>=DIMENSION:
        print("Wrong input!Your guess exceeds the board limit. Input again!",end="\n"*2)
        continue
    elif board[row_guess][col_guess] == 2: #2 stands for a marked wrong guess
        print("Wrong input!You already checked this location. Input again!",end="\n"*2)

    #Mark the guess and check whether player guess right:
    if board[row_guess][col_guess] == 1:
        right_guess = right_guess + 1
        print("You guess one right!",end="\n"*2)
        board[row_guess][col_guess] = 3 # 3 stands for a marked right guess
    else:
        board[row_guess][col_guess] = 2
        print("You guess wrong! Try again",end="\n"*2)
        
#End of the game:
print("Congratulations!You win the game:)",end="\n"*2)
print("You used",str(score),"times to win this game")

        
    
    
