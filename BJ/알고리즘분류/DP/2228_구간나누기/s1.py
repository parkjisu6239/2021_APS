import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
dp = dict()
result = -32768 * 100
for _ in range(N):
    arr.append(int(input()))


def get_section_max(idx, remain, total):
    global result
    if remain == 0:
        result = max(result, total)
        return

    if idx >= N:
        return

    if total < dp.get((idx, remain), -10000000000):
        return
    dp[(idx, remain)] = total

    for end in range(idx, N-(remain)*2+2):
        for start in range(end+2, N-(remain-1)*2+2):
            get_section_max(start, remain - 1, total + sum(arr[idx:end+1]))


for idx in range(N):
    get_section_max(idx, M, 0)

print(result)

