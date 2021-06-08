import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    rate = [ list(map(int, input().split())) for _ in range(N)]

    # 한명이 한개를 10000으로 먹으면 나머지 사람들 아무도 못먹음
    # 비율이 비슷비슷한 사람들한테 줘야 여러명한테 줄 수 있음
    # 1. 가장 작은 값을 먼저 넣거나(정렬 or min)
    # 2. 표준편차나 분산이 가장 적은 것부터 넣거나
    # 3. 완전 탐색으로 넣는 조합의 모든 경우의 수를 따져서 최대 개수를 구하거나

    ABC = [0, 0, 0]
    people = 0

