import sys
sys.stdin = open('input.txt')

# 00. input
N, M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

all_chicken = []
homes = []


# 01. 함수 정의
## 01-1. 치킨 집 조합 생성 함수
def Chicken_C_M(k, s, n, r): # k:선택된 조합 원소 개수, s: 구간 시작점, nCr
    if k == r:
        ckicken_combi.append(list(sel_ckicken))
        return

    for i in range(s, n-(r-k)+1):
        sel_ckicken[k] = all_chicken[i]
        Chicken_C_M(k+1, i+1, n, r)


## 01-2. 치킨 거리 구하는 함수
def Chicken_distance(ckickens):
    c_d = 0
    for hr, hc in homes:
        min_d = 999999999
        for cr, cc in ckickens:
            d = abs(hr - cr) + abs(hc - cc)
            if d < min_d:
                min_d = d
        c_d += min_d

    return c_d


# 02. 실행 부분
## 02-1. 집, 치킨집 리스트 생성
for i in range(N):
    for j in range(N):
        if land[i][j] == 1:
            homes.append((i, j))
        elif land[i][j] == 2:
            all_chicken.append((i, j))


## 02-2. (폐업X) 살아남은 치킨집 조합 생성 : 01-1 함수 실행
ckicken_combi = []
sel_ckicken = [0]*M
Chicken_C_M(0, 0, len(all_chicken), M)


## 02-3. 살아남은 치킨집 조합을 순회하여, 치킨 거리의 최솟값 구하기
min_c_d = 9999999999
for combi in ckicken_combi:
    temp_c_d = Chicken_distance(combi)
    if temp_c_d < min_c_d:
        min_c_d = temp_c_d


# 03. 결과 출력
print(min_c_d)
