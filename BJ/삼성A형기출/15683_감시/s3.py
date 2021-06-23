import sys
sys.stdin = open('input.txt')
q = lambda: map(int, sys.stdin.readline().split())

## 함수 1 ##
def getCctvArea(r, c, no):
    cctv_area = [{(r, c),} for _ in range(4)] # cctv의 4회전 감시 영역
    for k in range(4):
        nr, nc = r, c
        while True:
            nr += dr[k]
            nc += dc[k]
            if 0 <= nr < N and 0 <= nc < M and (not cctv[nr][nc] == 6):
                cctv_area[k].add((nr, nc))
                continue
            else:
                break

    if no == 1: # 4방향 모두 추가
        all_CCTV.append(cctv_area)
    elif no == 2: # 상하, 좌우 추가
        temp = [cctv_area[0]|cctv_area[2], cctv_area[1] | cctv_area[3]]
        all_CCTV.append(temp)
    elif no == 3: # ㄴ 모양 4방 회전 추가
        temp = [cctv_area[0]|cctv_area[1], cctv_area[1] | cctv_area[2], cctv_area[2] | cctv_area[3], cctv_area[3] | cctv_area[0]]
        all_CCTV.append(temp)
    elif no == 4: # ㅗ 모양 4방 회전 추가
        temp = [cctv_area[0] | cctv_area[1] | cctv_area[2],
                cctv_area[1] | cctv_area[2] | cctv_area[3],
                cctv_area[2] | cctv_area[3] | cctv_area[0],
                cctv_area[3] | cctv_area[0]| cctv_area[1]]
        all_CCTV.append(temp)
    else: # 전체 합쳐서 추가
        all_CCTV.append([cctv_area[0] | cctv_area[1] | cctv_area[2] | cctv_area[3]])


## 함수 2 ##
def dfs(n, union_set):
    global MAX
    if n==len(all_CCTV):
        if MAX < len(union_set):
            MAX = len(union_set)
        return
    for i in all_CCTV[n]:
        dfs(n+1, union_set|i)


## 입력 ##
N, M = q()
cctv = [list(q()) for _ in range(N)]


## global 변수 정의 ##
dr = [-1, 0, 1, 0] # 상 우 하 좌
dc = [0, 1, 0, -1]

# 각 CCTV 별로 모든 회전 상태를 담은 변수
# [[set(1번 cctv 감시 영역), set(1번 cctv 90도 회전 감시 영역),, ], [,,], ,,]
all_CCTV = []
empty = 0 # 벽이 아닌 칸의 수
MAX = 0

## 실행 ##
for n in range(N):
    for m in range(M):
        if 1 <= cctv[n][m] <= 5: # CCTV가 있는 곳 확인
            getCctvArea(n, m, cctv[n][m])
        if cctv[n][m] != 6:
            empty += 1

dfs(0, set())

## 출력 ##
print(empty - MAX)