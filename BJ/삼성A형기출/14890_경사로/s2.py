import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

N, L = q()
arr = [list(q()) for _ in range(N)]

# 1. high(idx+L) - high(idx) = 1 -> idx~idx+L-1에 경사로 건설, 전진 가능, 다음위치 idx+L
# 2. high(idx) - high(idx+1) = 1 -> idx+1~idx+L에 경사로 건설, 전진가능, 다음위치 idx+L
# 3. high(idx) = high(idx+1) -> 전진 가능, 다음위치 idx+1
# 4. else -> False

# 경사로 건설 가능한지 체크할 함수
# 재귀 돌릴 함수
# 경사로 건설, 건설 해제 할 함수

def isOK(r_c, RC, idx):
    if r_c == 'r':
        for i in range(idx, idx + L):
            if arr[RC][idx] != arr[RC][i]:
                return False

            if visit[RC][i]:
                return False
    else:
        for i in range(idx, idx + L):
            if arr[idx][RC] != arr[i][RC]:
                return False

            if visit[i][RC]:
                return False

    return True


def setRunway(r_c, RC, idx):
    if r_c == 'r':
        for i in range(idx, idx + L):
            visit[RC][i] = 1
    else:
        for i in range(idx, idx + L):
            visit[i][RC] = 1



def go_R(R, idx):
    if idx == N-1:
        return True

    if idx+L < N and arr[R][idx+L] - arr[R][idx] == 1 and isOK('r', R, idx):
        setRunway('r', R, idx)
        return go_R(R, idx+L)

    if idx+L < N and arr[R][idx] - arr[R][idx+1] == 1 and isOK('r', R, idx+1):
        setRunway('r', R, idx+1)
        return go_R(R, idx + L)

    if arr[R][idx] == arr[R][idx+1]:
        return go_R(R, idx + 1)

    return False


def go_C(C, idx):
    if idx == N-1:
        return True

    if idx+L < N and arr[idx+L][C] - arr[idx][C] == 1 and isOK('c', C, idx):
        setRunway('c', C, idx)
        return go_C(C, idx+L)

    if idx+L < N and arr[idx][C] - arr[idx+1][C] == 1 and isOK('c', C, idx+1):
        setRunway('c', C, idx+1)
        return go_C(C, idx + L)

    if arr[idx][C] == arr[idx+1][C]:
        return go_C(C, idx + 1)

    return False


result = 0

visit = [[0] * N for _ in range(N)]
for i in range(N):
    if go_R(i, 0):
        result += 1

visit = [[0] * N for _ in range(N)]
for i in range(N):
    if go_C(i, 0):
        result += 1

print(result)
