import sys
sys.stdin = open('input.txt')

## Que 구현 ##
def q_empty():
    global front, rear
    if front == rear: return True
    return False


def q_full():
    global front, rear
    if rear == Q_size-1: return True
    return False


def q_push(val):
    global front, rear
    if q_full():
        return
    rear += 1
    Q[rear] = val


def q_pop():
    global front, rear
    if q_empty():
        return
    front += 1
    return_val = Q[front]
    Q[front] = 0
    return return_val


## 함수 정의 ##

def cal_i(v, i):
    if i == 0: return v+1
    elif i == 1: return v-1
    elif i == 2: return v*2
    elif i == 3: return v-10


def BFS():
    visit = [-1] * 1000001
    visit[N] = 0

    while visit[M] == -1:
        v = q_pop()
        for i in range(4):
            w = cal_i(v, i)
            if 0 <= w <= 1000000 and visit[w] == -1:
                visit[w] = visit[v] + 1 # 연산 횟수 = N과의 거리
                q_push(w)

    return visit[M]


## 실행 ##
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    front, rear = -1, -1
    Q_size = 1000001
    Q = [0] * Q_size
    q_push(N)
    print('#{} {}'.format(tc, BFS()))


