import sys
import time
sys.stdin = open('input.txt')
start = time.time()
# 시작점 16개 선택, 시작점에서 4방 이동으로 가지 뻗기
# (이동 횟수, 토탈, 현위치)를 visit에 담고 있으면 안가기

def solution(r, c, total, move):
    global result
    if move == 6:
        result.add(total)
        return

    if total in visit[(r, c, move)]:
        return

    visit[(r, c, move)].append(total)

    if r+1 < 4:
        solution(r+1, c, total*10+arr[r+1][c], move+1)
    if r-1 >= 0:
        solution(r-1, c, total*10+arr[r-1][c], move+1)
    if c + 1 < 4:
        solution(r, c+1, total*10+arr[r][c+1], move+1)
    if c - 1 >= 0:
        solution(r, c-1, total*10+arr[r][c-1], move+1)


for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    # visit
    visit = {}
    for r in range(4):
        for c in range(4):
            for move in range(7):
                visit[(r, c, move)] = []

    result = set()

    # 모든 시작점
    for r in range(4):
        for c in range(4):
            # 행, 열, 토탈, 이동 횟수
            solution(r, c, arr[r][c], 0)

    print('#{} {}'.format(tc, len(result)))

print(time.time() - start)