import sys
sys.stdin = open("input.txt", "r")

def View(N, building):

    view_ok = 0
    for i in range(2, N-1):
        # 내 양옆 2개를 이웃으로 지정
        neighbors = building[i-2: i] + building[i+1: i+3]
        # 이웃중에 가장 큰 이웃 찾기
        max_neighbor = 0
        for neighbor in neighbors:
            if max_neighbor < neighbor:
                max_neighbor = neighbor

        # 내가 이웃보다 크면, 조망권확보세대 = 내 빌딩 높이 - 가장큰 이웃 높이
        if building[i] > max_neighbor:
            view_ok += building[i] - max_neighbor

    return view_ok

for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    print('#{} {}'.format(tc, View(N, building)))