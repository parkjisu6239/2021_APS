import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    # 서류, 면접 순위 각각 1~N위
    score = [list(map(int, input().split())) for _ in range(N)]

    resume = [0] * (N+1) # 이력서 idx 등의 interview 등수 value
    interview = [0] * (N+1) # 위랑 반대

    for r, i in score:
        resume[r] = i
        interview[i] = r

    result = 0

    for k in range(2, N+1): # 1등은 무조건이라 제외
        for l in range(1, k):
            if resume[l] < resume[k]:
                break
        else:
            result += 1

    print(result+1)
