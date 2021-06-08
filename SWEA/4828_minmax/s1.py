import sys
sys.stdin = open("eval_input.txt", "r")
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    my_max = numbers[0]
    my_min = numbers[0]

    for number in numbers:
        if my_max < number:
            my_max = number
        if my_min > number:
            my_min = number

    print('#{} {}'.format(tc, my_max - my_min))
'''

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    Bubble_sort(numbers)
    print('#{} {}'.format(tc, numbers[-1] - numbers[0]))

