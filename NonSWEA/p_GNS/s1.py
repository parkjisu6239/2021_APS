import sys
sys.stdin = open("eval_input.txt", "r")


def Weird_numbers_sort(N, Weird_numbers):
    # 카운팅 소트
    # 이상한 0~9 리스트 생성
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 이상한 숫자들의 등장 횟수를 세기 위한 변수 생성
    counter = [0] * 10
    # 이상한 숫자 리스트 길이 만큼(주어진 입력값 N)
    for i in range(N):
        # 이상한 리스트가 각 인덱스와 맞게 생성되어 있어서 인덱스 접근
        for j in range(10):
            # 이상한 숫자와 같은 경우 그때 인덱스의 값을 +1 해주고,
            # 반복을 줄이기 위해 break로 나가게 해줌
            if Weird_numbers[i] == num_list[j]:
                counter[j] += 1
                break

    # 정렬할 리스트 생성
    sorted_Weird_numbers = []
    # 0~9만큼
    for i in range(10):
        # 0~9에 쌓인 카운트수만큼 반복
        for _ in range(counter[i]):
            sorted_Weird_numbers.append(num_list[i])

    return ' '.join(sorted_Weird_numbers)


for _ in range(1, int(input())+1):
    tc, N = map(str, input().split())
    Weird_numbers = list(map(str, input().split()))
    print(tc)
    print(Weird_numbers_sort(int(N), Weird_numbers))