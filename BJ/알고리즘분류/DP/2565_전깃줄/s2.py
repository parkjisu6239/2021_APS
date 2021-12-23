import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort()

B = []
for a, b in AB:
    B.append(b)

print(B)
LIS = []
for idx in B:
    if not LIS:
        LIS.append(idx)
        continue

    if idx > LIS[-1]:
        LIS.append(idx)
    else:
        k = len(LIS)-1
        while k >= 0 and LIS[k] > idx:
            k -= 1

        LIS[k+1] = idx
    print(LIS)

print(N - len(LIS))