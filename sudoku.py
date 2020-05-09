def solver(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find


    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solver(bo):
                return True

            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num & pos[1] != i:
            return False
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num & pos[1] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for t in range(box_x * 3, box_x * 3 + 3):
            if bo[i][t] == num & (i, t) != pos:
                return False
    return True


def show_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
    for t in range(len(bo[0])):
        if t % 3 == 0 and t != 0:
            print(' | ', end="")

        if t == 8:
            print(bo[i][t])

        else:
            print(str(bo[i][t]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for t in range(len(bo[0])):
            if bo[i][t] == 0:
                return (i, t)  # row, column
    return None
