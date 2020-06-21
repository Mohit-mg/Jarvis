#--------global variables---------


#  Game board
board=["_","_","_",
       "_","_","_",
       "_","_","_"]

#if gAME IS STILL going
game_still_going= True


#who won? or tie?
winner=None

#who's turn it is 
current_player="X"

#display board 
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Play a game of tic tak toe
def play_game():
    #display initial board
    display_board()

    #while the game is still going on
    while game_still_going:

        #handle a single turn of an arbitary player
        handle_turn(current_player)


        #check if the game has ended
        check_if_gameover()


        #flip to the other player
        flip_turn()

    # the game is over
    if winner=="X" or winner=="O":
        print(f"{winner}.won")
    elif winner==None:
        print("Tie.")

# Handle a single turn of arbitary player
def handle_turn(player):

    print(player +"'s turn.")
    position=input("choose a position between 1 to 9:")
    valid= False
    while not valid:
        
        while position not  in  ["1","2","3","4","5","6","7","8","9"]:
            position=input("invalid input. choose a position between 1 to 9:")
            
        position=int(position)-1

        if board[position] =="_":
            valid =True
        else:
            print("you can't enter again same position its occupied:")
            
    board[position]=player
    display_board()

def check_if_gameover():
    #if win
    # if game is tie
    win()
    tie()
    return

def win():

    global winner
    #check row
    row_winner=check_rows()
    #check column
    column_winner=check_columns()
    #check diagonals
    diagonal_winner=check_digonals()
    if row_winner:
        winner=row_winner
        #there was a win
    elif column_winner:
        winner=column_winner
        #there was a win
    elif diagonal_winner:
        winner=diagonal_winner
        #there was a win
    else:
        winner=None
    return

def check_rows():
    #set up global variable
    global game_still_going
    #
    row1=board[0]==board[1]==board[2] !="_"
    row2=board[3]==board[4]==board[5] !="_"
    row3=board[6]==board[7]==board[8] !="_"
    if row1 or row2 or row3 :
        game_still_going =False
    # return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
       #set up global variable
    global game_still_going
    #
    clm1=board[0]==board[3]==board[6] !="_"
    clm2=board[1]==board[4]==board[7] !="_"
    clm3=board[2]==board[5]==board[8] !="_"
    if clm1 or clm2 or clm3 :
        game_still_going =False
    # return the winner (X or O)
    if clm1:
        return board[0]
    elif clm2:
        return board[1]
    elif clm3:
        return board[2]
    return
    

def check_digonals():
       #set up global variable
    global game_still_going
    #
    dig1=board[0]==board[4]==board[8] !="_"
    dig2=board[2]==board[4]==board[6] !="_"
    
    if dig1 or dig2:
        game_still_going =False
    # return the winner (X or O)
    if dig1:
        return board[0]
    elif dig2:
        return board[2]
    return
    

def tie():
    global game_still_going
    if"_" not in board:
        game_still_going=False
    return

def flip_turn():
    #global variables we need
    global current_player
    #if the current player was x, then change it to o
    if current_player=="X":
        current_player="O"
    #if current player was o then the chnage it to x
    elif current_player =="O":
        current_player="X"

    return
if __name__ == "__main__":
    play_game()