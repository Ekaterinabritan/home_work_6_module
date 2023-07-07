import random

def is_queen_beat(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []
    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    list_chess = [[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]
    print(is_queen_beat(list_chess))