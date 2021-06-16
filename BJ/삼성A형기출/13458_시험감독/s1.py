import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for student in A:
    # 총감독 배치
    cnt += 1
    student = student - B

    # 부감독 배치
    if student > 0:
        cnt += student // C
        if student % C > 0: cnt += 1

print(cnt)

