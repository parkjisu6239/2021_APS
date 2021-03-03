import sys
sys.stdin = open("input.txt", "r")

N = int(input())

# 1.1
'''
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(arr)
'''

# 1.2
'''
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

print(arr)
'''

# 1.3
arr = [ list(map(int, input().split())) for _ in range(N) ]
print(arr)

# 2.1 행우선
for i in range(N):
    for j in range(N):
        print(arr[i][j])
print()

# 2.2 행우선 reverse
for i in range(N):
    for j in range(N-1, -1, -1):
        print(arr[i][j])
print()

# 3.1 열우선
for i in range(N):
    for j in range(N):
        print(arr[j][i])
print()

# 3.2 열우선 reverse
for i in range(N):
    for j in range(N-1, -1, -1):
        print(arr[j][i])
print()

# 4 지그재그
for i in range(N):
    for j in range(N):
        print(arr[i][j + (N-1-2*j) * (i%2)])
print()

# 5 전치행렬
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
print()