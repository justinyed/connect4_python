from sys import exit
from time import sleep
from random import randint

# 6 by 7 Empty Board
row0 = [" ", " ", " ", " ", " ", " ", " "]
row1 = [" ", " ", " ", " ", " ", " ", " "]
row2 = [" ", " ", " ", " ", " ", " ", " "]
row3 = [" ", " ", " ", " ", " ", " ", " "]
row4 = [" ", " ", " ", " ", " ", " ", " "]
row5 = [" ", " ", " ", " ", " ", " ", " "]
empty_board = [row0, row1, row2, row3, row4, row5]


def board_print(board):
    n_row = 7

    for row in board:
        n_row -= 1
        print(f"{n_row}  [{row[0]}][{row[1]}][{row[2]}][{row[3]}][{row[4]}][{row[5]}][{row[6]}]")

    print("\n    1  2  3  4  5  6  7")
    print("-" * 24)
    return None


def drop(board, x, puck):
    for y in range(1, 7):
        if board[6 - y][(x - 1)] == " ":
            board[6 - y][(x - 1)] = puck
            break
        elif y == 6:
            raise Exception("Column is Full; Try Again")
    return board


def winner(winner, board, turn, how):
    print("\n" * 50)
    print(f"Turn(s): {turn}")
    print("-" * 24)
    board_print(board)
    print(f"\nWINNER: {winner} --- {how}")
    exit()


def get_coord(x, y, board):
    return board[6 - y][(x - 1)]


def check_dia(x, y, n, board, turn):
    count = 0
    last = " "
    if y == 1:
        if x == 1:
            length = 6
        elif x == 2:
            length = 6
        elif x == 3:
            length = 5
        elif x == 4:
            length = 4
    if x == 1:
        if y == 1:
            length = 6
        elif y == 2:
            length = 5
        elif y == 3:
            length = 4

    for m in range(length):
        cur = get_coord(((-1) ** (n + 1)) * (x + m) + (0 ** n), (y + m), board)

        if cur != "O" and cur != "X":
            count = 0
        elif cur == last:
            count += 1
        else:
            count = 1

        if count == 4:
            how = "Won by diagonal"
            winner(cur, board, turn, how)
        # print("m:", m, "cur:", cur, "last:", last, "count:", count)
        last = cur
    return None


def check(board, turns):
    for row in board:  # Check Horizontals
        count = 0
        last = " "

        for n_col in range(len(row)):
            cur = row[n_col]

            if cur != "O" and cur != "X":
                count = 0
            elif cur == last:
                count += 1
            else:
                count = 1

            if count == 4:
                how = "Won by horizontal"
                winner(cur, board, turns, how)
            # print("col:", col, "y:", y, "cur:", cur, "last:", last, "count:", count)
            last = cur

    for col in range(1, 8):  # Check Verticals
        count = 0
        last = " "
        x = col
        y = 1

        for y in range(1, 7):
            cur = get_coord(x, y, board)

            if cur != "O" and cur != "X":
                count = 0
            elif cur == last:
                count += 1
            else:
                count = 1

            if count == 4:
                how = "Won by vertical"
                winner(cur, board, turns, how)
            # print("col:", col, "y:", y, "cur:", cur, "last:", last, "count:", count)
            last = cur

    # Check Different diagonal angles
    for nth_col in range(1, 5):
        x = nth_col
        y = 1
        n = 1
        check_dia(x, y, n, board, turns)

    for nth_row in range(1, 4):
        x = 1
        y = nth_row
        n = 1
        check_dia(x, y, n, board, turns)

    for nth_col in range(1, 5):
        x = nth_col
        y = 1
        n = 0
        check_dia(x, y, n, board, turns)

    for nth_row in range(1, 4):
        x = 1
        y = nth_row
        n = 0
        check_dia(x, y, n, board, turns)

    return None


def menu(board, turn):
    print("\n" * 50)
    print("Turn(s):", turn)
    print("-" * 24)
    board_print(board)

    if turn % 2 == 0:  # Take Turns
        puck = "X"
    else:
        puck = "O"

    try:    # Drop Puck into Column
        # col = randint(1, 7)   # Generate Random Games
        col = int(input(f"Player {puck}, drop in what column: "))
        if 0 < col <= 7:
            drop(board, col, puck)
        else:
            raise Exception("Column Out of Range; Try Again")
    except ValueError as val_error:
        print("Improper Input; Try Again")
        sleep(0.75)
        menu(board, turn)
    except Exception as error:
        print(error)
        sleep(0.75)
        menu(board, turn)

    check(board, turn)  # Check board fro connect 4's including diagonal, horizontal, and vertical.

    if turn == 42:  # Tie Game
        print("\n" * 50)
        print("Tie, Max number of turns has been reached")
        exit()

    menu(board, turn + 1)  # Increment Turn and Continue to next turn


if __name__ == '__main__':
    menu(empty_board, turn=0)  # Start New Game
