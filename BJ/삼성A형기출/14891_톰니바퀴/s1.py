import sys
sys.stdin = open('input.txt')

# 6, 2번 인덱스 좌우랑 맞닿는 부분
# 시계방향으로 돌면 list의 원소들 오른쪽으로 이동
# 반시계 방향으로 돌면 list의 원소들 왼쪽으로 이동

def rotate(idx, direction):
    if direction == 1: # 시계 방향
        gear[idx] = [gear[idx][-1]] + gear[idx][:-1]
    else: # 반시계 방향
        gear[idx] = gear[idx][1:] + [gear[idx][0]]


gear = [[0]]
for _ in range(4):
    gear.append(list(map(int, input())))

K = int(input())
for _ in range(K):
    idx, direction = map(int, input().split())
    rotate_temp = [(idx, direction)]
    if idx == 1:
        for i in range(3):
            if gear[idx+i][2] != gear[idx+i+1][6]:
                rotate_temp.append((idx+i+1, direction*((-1)**(i+1))))
            else:
                break
    elif idx == 2:
        if gear[idx-1][2] != gear[idx][6]:
            rotate_temp.append((idx-1, direction*-1))

        for i in range(2):
            if gear[idx+i][2] != gear[idx+i+1][6]:
                rotate_temp.append((idx+i+1, direction*((-1)**(i+1))))
            else:
                break
    elif idx == 3:
        for i in range(4):
            if gear[idx-i-1][2] != gear[idx-i][6]:
                rotate_temp.append((idx-i-1, direction*((-1)**(i+1))))
            else:
                break

        if gear[idx][2] != gear[idx+1][6]:
            rotate_temp.append((idx+1, direction*-1))
    else:
        for i in range(3):
            if gear[idx-i-1][2] != gear[idx-i][6]:
                rotate_temp.append((idx-i-1, direction*((-1)**(i+1))))
            else:
                break

    for index, d in rotate_temp:
        rotate(index, d)


SUM = 0
for g in range(4):
    SUM += gear[g+1][0]*(2**g)

print(SUM)