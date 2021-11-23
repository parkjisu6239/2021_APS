import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))


ans = [[0, -1, -1] for _ in range(N)]

left = []
for i in range(N):
    while left and buildings[left[-1]] <= buildings[i]:
        left.pop()
    left.append(i)
    if len(left) > 1:
        ans[i][0] += len(left) - 1
        ans[i][1] = left[-2]


right = []
for i in range(N-1, -1, -1):
    while right and buildings[right[-1]] <= buildings[i]:
        right.pop()
    right.append(i)
    if len(right) > 1:
        ans[i][0] += len(right) - 1
        ans[i][2] = right[-2]


for i in range(N):
    if ans[i][0]:
        if ans[i][1] != -1 and ans[i][2] != -1:
            print(ans[i][0], ans[i][1]+1 if i - ans[i][1] <= ans[i][2] - i else ans[i][2]+1)
        elif ans[i][1] != -1:
            print(ans[i][0], ans[i][1]+1)
        elif ans[i][2] != -1:
            print(ans[i][0], ans[i][2]+1)
    else:
        print(0)

