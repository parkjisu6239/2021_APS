import sys
sys.stdin = open("eval_input.txt", "r")

# input
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    gravity = list(map(int, input().split()))

    # 가장 큰 낙차 초기화
    max_fall = 0
    # gravity 순회
    for i in range(N):
        # 해당 인덱스의 낙차 초기화
        fall = 0
        # 다음에 나오는 블럭들이랑 길이 비교할거라서 i+1부터 순회
        for j in range(i+1, N):
            # 현재 박스의 길이가 내 다음에 나오는 것들보다 클 때만 낙차 1씩 더하기
            if gravity[i] > gravity[j]:
                fall += 1
        # 현재 인덱스의 낙차 계산이 완료되면, 최댓값일 경우 최대값으로 지정
        if max_fall < fall:
            max_fall = fall

    print('#{} {}'.format(tc, max_fall))