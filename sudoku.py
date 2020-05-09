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
