import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    corridor = [0] * 401
    for _ in range(N):
        start, end = map(int, input().split())

        # 편의상 작은방 > 큰방 이동으로
        if start > end: start, end = end, start

        # 시작점이 짝수이면 마주보는 홀수방과 같은 복도를 공유하게 됨
        # 도착점이 홀수이면 마주보는 짝수방과 같은 복도를 공유하게 됨
        if start % 2 == 0: start -= 1
        if end % 2 : end += 1

        # 해당 학생이 시작점에서 도착점으로 돌아가는 동안 지나간 복도를 표시함
        for i in range(start, end + 1):
            corridor[i] += 1

    # 복도는 해당 인덱스를 지나간 사람 수가 기록됨
    # 복도의 최대값은 그 복도를 지나가는 사람수이고, 그때 그 학생들은 동시에 지나갈 수 없어서 그 값만큼의 시간이 소요됨
    # 그 복도를 지나지 않는 다른 학생들은 동시에 움직일 수 있으니, 시간 고려 X
    print('#{} {}'.format(tc, max(corridor)))