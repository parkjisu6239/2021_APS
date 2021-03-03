import sys
sys.stdin = open("input.txt")

def Harvest(n, farm):
    result = 0

    # 열 인덱스 n // 2를 중심으로 좌우를 가져옴 = farm[i][n // 2] 각 행의 중심 열
    for i in range((n // 2) + 1): # 행은 중간 까지만(좌우 대칭이라 한번에 더하기 위해서)
        if i != n // 2: # 중앙행이 아니면, 양쪽 좌우대칭이라 한번에 두개 더하기
            result += sum(farm[i][(n//2)-i: (n//2)+i+1]) + sum(farm[n-1-i][(n//2)-i: (n//2)+i+1])
        else: # 중앙행은 1개 뿐이라 그거만 더하기
                result += sum(farm[i][(n//2)-i: (n//2)+i+1])

    return result

for tc in range(1, int(input())+1):
    n = int(input())
    farm = [ list(map(int, input())) for _ in range(n) ]
    print('#{} {}'.format(tc, Harvest(n, farm)))