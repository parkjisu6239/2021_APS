import sys
sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt')
input = sys.stdin.readline

length, width, height = map(int, input().split())
n = int(input())

cubes = [0] * n
for _ in range(n):
    a, b = map(int, input().split())
    cubes[a] = b

total = 0
count = 0
for i in range(n-1, -1, -1):
    total <<= 3
    t = min(cubes[i], (length >> i)*(width >> i)*(height >> i) - total)
    total += t
    count += t

if(total == length*width*height):
    print(count)
else:
    print(-1)
