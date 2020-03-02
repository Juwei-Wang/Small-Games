import sys
import random


def count_neighbours(i, j, board):
    count = 0
    for i_off in range(-1, 2):
        for j_off in range(-1, 2):
            if board[i + i_off][j + j_off]:
                count += 1
    return count


n = int(sys.argv[1])
m = int(sys.argv[2])
mine_count = (n * m) // 2

# n tall
# m wide
# column major

column = [False] * (n + 2)
board = []
for r in range(m + 2):
    board += [column.copy()]

for i in range(mine_count):
    x = random.randrange(1, m + 1)
    y = random.randrange(1, n + 1)
    board[x][y] = True

for j in range(1, n + 1):
    for i in range(1, m + 1):
        if board[i][j]:
            print('*', end=' ')
        else:
            neighbour_count = count_neighbours(i, j, board)
            print(neighbour_count, end=' ')
    print('\n', end='')
pass
