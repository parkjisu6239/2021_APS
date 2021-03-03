import sys
sys.stdin = open("input.txt")

def Hyunju_Box(N, Q):
    # 박스의 길이는 N, 모든 값은 0으로 초기화
    boxes = [0] * N
    # Q만큼 반복할건데 넣어야하는 숫자가 첫번째 줄이니까 1을 넣는다고 했으므로,
    # 인덱스 0이 아닌 1부터 시작하려고 range(1, Q+1)로 작성
    for number in range(1, Q+1):
        # 좌,우 입력받음
        L, R = map(int, input().split())
        # 입력받은건 0번째부터 시작이 아니라, 첫번째 부터 시작하는 의미라서
        # 박스의 인덱스는 0부터 시작하기 때문에 range(L-1, R)로 작성
        for i in range(L-1, R):
            boxes[i] = number

    return ' '.join(map(str, boxes))

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    print('#{} {}'.format(tc, Hyunju_Box(N, Q)))