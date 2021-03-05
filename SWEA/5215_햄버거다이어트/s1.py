import sys
sys.stdin = open('input.txt')

def DFS(idx):
    global score, max_score, calorie

    # 부분집합이 모두 구해졌다면
    if idx == N:
        if calorie < L and score > max_score:
            max_score = score
        return

    # 유망하지 않음
    if calorie > L : return

    # 재료를 안 넣거나
    sel[idx] = 0
    DFS(idx+1)

    # 재로를 넣거나
    sel[idx] = 1
    score += ingredients[idx][0]
    calorie += ingredients[idx][1]
    DFS(idx + 1)
    # 재귀나와서는 이전에 더 했던 값 빼야함(원상복구)
    score -= ingredients[idx][0]
    calorie -= ingredients[idx][1]



for tc in range(1, int(input())+1):
    # 재료수, 칼로리 제한
    N, L = map(int, input().split())
    # 맛점수, 칼로리
    ingredients = [ list(map(int, input().split())) for _ in range(N)]

    # 부분집합을 구하되, 제한 칼로리를 넘으면 백트래킹!
    # 점수가 높으면 갱신!

    # 재료의 선택 유무 표현
    sel = [0] * N

    # 최고점
    max_score = 0
    calorie = 0
    score = 0

    DFS(0)
    print('#{} {}'.format(tc, max_score))

