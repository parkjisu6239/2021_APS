import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)
result = []


def chain(x):
    temp = [x]
    while arr[x] not in temp:
        x = arr[x]
        temp.append(x)

    if arr[x] == temp[0]:
        result.extend(temp)


for i in range(1, N+1):
    arr[i] = int(input())


for i in range(1, N+1):
    if i in result:
        continue

    if i == arr[i]:
        result.append(i)
    else:
        chain(i)

print(len(result))
print(*sorted(result), sep="\n")


