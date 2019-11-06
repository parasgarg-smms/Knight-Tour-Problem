import time


def print_boaord(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")


def return_possible_values(board, current_position):
    a, b = current_position
    arr = []
    arr.extend(((+2 + a, +1 + b), (+2 + a, -1 + b), (-2 + a, +1 + b), (-2 + a, -1 + b)))
    arr.extend(((+1 + a, +2 + b), (+1 + a, -2 + b), (-1 + a, +2 + b), (-1 + a, -2 + b)))
    temp = arr.copy()
    for i in arr:
        x, y = i
        try:
            if board[x][y] == -1 and x > -1 and y > -1 and x < 8 and y < 8:
                continue
            else:
                temp.remove(i)
        except:
            temp.remove(i)
    return temp


def solve(board, n, current_pos=(0, 0)):
    if n >= 63:
        return True
    arr = return_possible_values(board, current_pos)
    for i in arr:
        x, y = i
        if board[x][y] != -1:
            return False
        board[x][y] = n
        if solve(board, n + 1, (x, y)):
            return True
        board[x][y] = -1
    return False


board = [
    [0, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],

]

if __name__ == '__main__':
    print_boaord(board)
    print("")
    start = time.process_time()
    solve(board, 1)
    over = time.process_time()
    print(over - start)
    print_boaord(board)
