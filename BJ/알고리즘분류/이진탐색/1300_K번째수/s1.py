import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
k = int(input())

l, r = 1, N*N

# [1, 2, 2, 3, 3, 4, 6, 6, 9]
while l <= r:
    m = (l + r) //  2

    cnt = 0
    for i in range(1, m+1):
        for j in range(1, min(N, i) + 1):
            if i % j == 0 and i // j <= N:
                cnt += 1

    if cnt == k :
        print(m)
        break
    elif cnt < k:
        l = m + 1
    else:
        r = m - 1



arr = [(i+1)*(j+1)for i in range(N) for j in range(N)]
arr.sort()
print(arr)