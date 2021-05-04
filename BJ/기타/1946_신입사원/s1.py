import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    # 서류, 면접 순위 각각 1~N위
    score = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(len(score)):
        for j in range(len(score)):
            if i != j and (score[i][0] > score[j][0] and score[i][1] > score[j][1]):
                break
        else:
            result += 1

    print(result)
