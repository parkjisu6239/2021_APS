import sys

sys.stdin = open("input.txt", "r")


def Weird_numbers_sort(N, Weird_numbers):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_dict = dict()
    for num_str in num_list:
        count_dict[num_str] = 0

    for Weird_number in Weird_numbers:
        count_dict[Weird_number] = count_dict.get(Weird_number, 0) + 1

    sorted_Weird_numbers = []
    for key, val in count_dict.items():
        for _ in range(val):
            sorted_Weird_numbers.append(key)

    return ' '.join(sorted_Weird_numbers)


for _ in range(1, int(input()) + 1):
    tc, N = map(str, input().split())
    Weird_numbers = list(map(str, input().split()))
    print(tc)
    print(Weird_numbers_sort(int(N), Weird_numbers))