import sys
sys.stdin = open("input.txt")

def GeneralQuickSort(numbers, start, end):
    if start < end:
        p = Partition(numbers, start, end)
        GeneralQuickSort(numbers, start, p-1)
        GeneralQuickSort(numbers, p+1, end)
    return numbers

def Partition(numbers, start, end):
    # 왼,오,피봇은 numbers의 인덱스
    pivot = start
    L = start + 1
    R = end
    done = False # 분할 완료 플래그

    while not done:
        # 피봇을 기준으로 작은건 왼쪽 큰건 오른쪽에 모이도록 교환한다.
        while L <= R and numbers[L] <= numbers[pivot]: L += 1
        while L <= R and numbers[R] >= numbers[pivot]: R -= 1

        if L < R:
            numbers[L], numbers[R] = numbers[R], numbers[L]
        # 모든 교환이 일어나서 L과 R이 교차되면 교환을 종료한다.
        else:
            done = True

    # 교환이 종료된 경우 작은게 모여있는 왼쪽, 큰게 모여있는 오른쪽 중간에 피벗을 위치시켜야 한다.
	# 위에서 종료된 경우, 0~R까지는 은 피벗보다 작은 값들이 있고
	# R+1부터 끝까지는 피벗보다 큰 수가 위치한다.
	# 즉 R과 피벗을 교환하여 피벗의 위치를 고정 시키고 피벗 좌우로 작은값/큰값이 분할 완료한다.
    numbers[pivot], numbers[R] = numbers[R], numbers[pivot]
    return R


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    GeneralQuickSort(numbers, 0, len(numbers)-1)
    print('#{}'.format(tc), end=" ")
    print(*numbers)