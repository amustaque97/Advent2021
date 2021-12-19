def check_horizontal(board, x):
    for i in range(0, 5):
        if board[x][i] != -1:
            return False
    return True

def check_vertical(board, y):
    for i in range(0, 5):
        if board[i][y] != -1:
            return False
    return True

with open('input.txt') as f:
    moves = []
    board = []
    players = []
    for line in f.readlines():
        if ',' in line:
            moves = line.replace('\n', '').split(',')
        else:
            line = line.replace('\n', '')
            if len(line) == 0:
                players.append(board)
                board = []
            else:
                elements = line.split()
                board.append(elements)
    # adding last board
    players.append(board)

    del players[0]

    #print board for all players
    #for board in players:
    #    for row in board:
    #        print(row)
    #    print()

    winning_move = 0
    winner_board = [] # this variable will store winning board
    for move in moves:
        for board in players:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == move:
                        board[i][j] = -1
                        if check_horizontal(board, i) or check_vertical(board, j):
                            winning_move = move
                            winner_board = board
                            break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

    total = 0 # calculate total value
    for row in winner_board:
        for ele in row:
            if int(ele) != -1:
                total += int(ele)

    print(total, winning_move)
    print(total * int(winning_move))
