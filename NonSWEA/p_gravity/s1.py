import sys

sys.stdin = open("input.txt", "r")

#1. input 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    # 2. 결과 저장
    gravity = []
    # 방의 크기 만큼 반복
    for i in range(N):
        # 낙차를 구할 정수 할당
        gra = 0
        # 첫번째 상자부터, 다음 상자랑 비교 반복할 것
        for j in range(i+1, N):
            # 첫번째 상자의 길이가 다음에 나오는 상자보다 길면 낙차 발생
            if box_list[i] > box_list[j]:
                gra += 1
                gravity.append(gra)

    # 발생하는 낙차 중에서 가장 큰 값만 반환
    print('#{} {}'.format(tc, max(gravity)))