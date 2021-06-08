import sys
sys.stdin = open('eval_input.txt', 'r')

def Patition(arr, l, r):
    p = arr[l] # 왼쪽 끝값
    i, j = l, r # ->, <- 방향으로 이동할 인덱스

    while i <= j: # 왼,오 교차되기 전까지
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i] # 작은거 <-> 큰거 💛

    # [*왼, 피봇, *오] 로 만들기 위해서 왼오 사이에 피봇을 넣어야한다.
    # i, j가 교차된 경우 여기로 도달하게 되기때문에
    # (중요!) j는 피봇보다 작은 수 중에서 가장 오른쪽에 있는 인덱스를 뜻한다.💛
    arr[l], arr[j] = arr[j], arr[l] # 💛

    return j # 피봇 인덱스, 위치 고정 완료 # 💛


def Quick_Sort(arr, l, r): # 분할
    if l < r:
        # 파티션 함수를 사용하여 피봇을 기준으로 작은거 왼쪽, 큰거 오른쪽
        # 즉, 피봇 위치는 고정된다. 사실 파티션 함수가 실제 정렬을 담당.
        pivot = Patition(arr, l, r)

        # 그래서 피봇은 더이상 정렬에 포함하지 않는다.
        Quick_Sort(arr, l, pivot-1)
        Quick_Sort(arr, pivot+1, r)


for tc in range(1, int(input())+1):
    N = int(input())
    number = list(map(int, input().split()))
    Quick_Sort(number, 0, len(number)-1)
    print('#{} {}'.format(tc, number[N // 2]))
