import sys
sys.stdin = open('input.txt')


# 상하 앞뒤 좌우
cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
        ]

# LR 회전(시계) : 상 -> 앞 -> 하 -> 뒤 -> 상 ; 0 2 1 3
# FB 회전(시계) : 상 -> 우 -> 하 -> 좌 -> 상 ; 0 5 2 4
# UD 회전(시계) : 앞 -> 좌 -> 뒤 -> 우 -> 앞 ; 2 4 3 5
rotate = {
        'L': [0, 2, 1, 3, 0],
        'R': [0, 2, 1, 3, 0],
        'F': [0, 5, 2, 4, 0],
        'B': [0, 5, 2, 4, 0],
        'U': [2, 4, 3, 5, 2],
        'D': [2, 4, 3, 5, 2],
        }

def move(d, o):
    oerder = rotate[d]

    if d == 'L' or d == 'R':
        k = 0 if d == 'L' else 2
        for i in range(4):
            if o == '+':
                print(oerder[4-i], '->', oerder[4-i-1])
                cube[oerder[4-i]][0][k] = cube[oerder[4-i-1]][0][k]
                cube[oerder[4-i]][1][k] = cube[oerder[4-i-1]][1][k]
                cube[oerder[4-i]][2][k] = cube[oerder[4-i-1]][2][k]
            else:
                print(oerder[i+1], '->', oerder[i])
                cube[oerder[i]][0][k] = cube[oerder[i+1]][0][k]
                cube[oerder[i]][1][k] = cube[oerder[i+1]][1][k]
                cube[oerder[i]][2][k] = cube[oerder[i+1]][2][k]

    elif d == 'U' or d == 'D':
        k = 0 if d == 'U' else 2
        for i in range(4):
            if o == '+':
                print(oerder[4 - i], '->', oerder[4 - i - 1])
                cube[oerder[4 - i]][k][0] = cube[oerder[4 - i - 1]][k][0]
                cube[oerder[4 - i]][k][1] = cube[oerder[4 - i - 1]][k][1]
                cube[oerder[4 - i]][k][2] = cube[oerder[4 - i - 1]][k][2]
            else:
                print(oerder[i + 1], '->', oerder[i])
                cube[oerder[i]][k][0] = cube[oerder[i + 1]][k][0]
                cube[oerder[i]][k][1] = cube[oerder[i + 1]][k][1]
                cube[oerder[i]][k][2] = cube[oerder[i + 1]][k][2]



N = int(input())
for _ in range(N):
    M = int(input())
    cmd = input().split()
    for command in cmd:
        d, o = command
        move(d, o)
