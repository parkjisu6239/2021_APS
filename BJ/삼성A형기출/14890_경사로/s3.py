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


def isOK(R, idx):
    for i in range(idx, idx + L):
        if arr[R][idx] != arr[R][i]:
            return False
    return True

def go(R, idx):
    if idx == N-1:
        return True

    if idx+L < N and arr[R][idx+L] - arr[R][idx] == 1 and isOK(R, idx):
        return go(R, idx+L)

    if idx+L < N and arr[R][idx] - arr[R][idx+1] == 1 and isOK(R, idx+1):
        return go(R, idx + L)

    if arr[R][idx] == arr[R][idx+1]:
        return go(R, idx + 1)

    return False

result = 0
for i in range(N):
    if go(i, 0): result += 1

arr = list(zip(*arr))
for i in range(N):
    if go(i, 0): result += 1

print(result)
