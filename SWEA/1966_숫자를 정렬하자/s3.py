import sys
sys.stdin = open("eval_input.txt")

def QuickSort(numbers):
    # 길이가 0,1 이면 정렬 필요 없이 그대로 리턴(베이스 케이스)
    if len(numbers) < 2:
        return numbers

    # 길이가 2 이상이라면 아래 과정을 수행
    # 왼, 오, 피벗 지정
    left = []
    right = []
    pivot = numbers[0]

    # numbers의 길이만큼 순회, 0은 위에서 피벗으로 고정했으니까 1부터 순회
    for i in range(1, len(numbers)):
        # 피벗보다 크거나 같으면 오른쪽
        if numbers[i] >= pivot:
            right.append(numbers[i])
        # 피벗보다 작으면 왼쪽
        else:
            left.append(numbers[i])

    # 나누어진 왼쪽, 오른쪽에 대해서 퀵정렬을 다시 수행한다.
    # 왼, 오가 각각 자신의 피벗,왼,오를 지정하고 위 과정을 반복하여 최종 결과물을 return 한다.
    return [*QuickSort(left)] + [pivot] + [*QuickSort(right)]


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{}'.format(tc), end=" ")
    print(*QuickSort(numbers))