import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

for i in range(N):
    left = [i]
    for j in range(1, i+1):
        if buildings[i-j] > buildings[left[-1]]:
            left.append(i-j)
    right = [i]
    for k in range(1, N-i):
        if buildings[i+k] > buildings[right[-1]]:
            right.append(i+k)

    cnt = len(left) + len(right) - 2
    if len(left) > 1 and len(right) > 1:
        if i - left[1] <= right[1] - i:
            print(cnt, left[1]+1)
        else:
            print(cnt, right[1]+1)
    elif len(left) > 1:
        print(cnt, left[1]+1)
    elif len(right) > 1:
        print(cnt, right[1]+1)
    else:
        print(0)