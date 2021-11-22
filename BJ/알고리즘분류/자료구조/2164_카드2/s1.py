import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(range(1, N+1))

while arr:
    arr.pop(0)

    if len(arr) > 1:
        arr.append(arr.pop(0))
    else:
        print(arr[0])
        break