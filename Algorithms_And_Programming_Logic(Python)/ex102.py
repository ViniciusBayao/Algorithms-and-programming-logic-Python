"""
Create a Tic-Tac-Toe(Python) using matrix(mathematics), nested list(Programming, Python).
"""


def ticTacToe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    over = False
    magic_square = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    def DisplayBoard():
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()

    def GetNumber():
        while True:
            number = input()
            try:
                number = int(number)
                if number in range(1, 10):
                    return number
                else:
                    print("\nThe number is not on the board.")
            except ValueError:
                print("\nThis is not a number. Try again.")
                continue

    def Round(player):
        filled_space = GetNumber() - 1
        if board[filled_space] == "X" or board[filled_space] == "O":
            print("\nSpace already filled. Try to put in another one.")
            Round(player)
        else:
            board[filled_space] = player

    def VerifyVictory(player):
        moves = 0

        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if board[x] == player and board[y] == player and board[z] == player:
                            if magic_square[x] + magic_square[y] + magic_square[z] == 15:
                                print("Player", player, "won!\n")
                                return True

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                moves += 1
            if moves == 9:
                print("The game ended in a tie\n")
                return True

    while not over:
        DisplayBoard()
        over = VerifyVictory("O")
        if over:
            break
        print("Player 1, Choose an space: ")
        Round("X")

        DisplayBoard()
        over = VerifyVictory("X")
        if over:
            break
        print("Player 2, Choose an space: ")
        Round("O")


ticTacToe()
