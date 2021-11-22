import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "pop":
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if len(arr):
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if len(arr):
            print(arr[-1])
        else:
            print(-1)


