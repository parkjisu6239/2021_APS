import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline().rstrip()
lst = [0] * 2020001

N = int(input)

answer = 'YES'
for i in range(N):
    x, r = map(int, input.split())
    if lst[x - r + 1010000] or lst[x + r + 1010000]: # 접점 한 개
        answer = 'NO'
        break
    elif sum(lst[x - r + 1010000:x + r + 1010000 + 1]) % 3: # 접점 두 개
        answer = 'NO'
        break
    lst[x - r + 1010000] = 1
    lst[x + r + 1010000] = 2

print(answer)