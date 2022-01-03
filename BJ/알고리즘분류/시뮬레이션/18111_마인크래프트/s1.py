import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]


def get_info():
    MIN, MAX, temp = 256, 0, dict()
    for i in range(N):
        for j in range(M):
            MIN = min(MIN, land[i][j])
            MAX = max(MAX, land[i][j])
            temp[land[i][j]] = temp.get(land[i][j], 0) + 1

    return MIN, MAX, temp


def flat(target):
    inven = B
    time = 0
    for height, cnt in blocks.items():
        if height > target:
            inven += (height - target)*cnt
            time += 2*(height - target)*cnt
        elif height < target:
            inven -= (target - height) * cnt
            time += (target - height) * cnt

    if inven >= 0:
        return time
    else:
        return 999999999


minH, maxH, blocks = get_info()
result = 999999999
H = 0

for val in range(minH, maxH+1):
    ans = flat(val)
    if ans <= result:
        result = ans
        H = val

print(result, H)
