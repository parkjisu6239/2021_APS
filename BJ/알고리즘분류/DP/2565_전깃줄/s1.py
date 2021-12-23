import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    a, b = map(int, input().split())
    lines.append([a, b])

cut = [0] * N
min_cut = 101


def is_cross(idx):
    for i in range(N):
        if cut[i]: # 자른건 pass
            continue

        if idx == i: # 자기자신은 pass
            continue

        if (lines[idx][0] - lines[i][0])*(lines[idx][1] - lines[i][1]) < 0:
            return True

    return False


def cut_line(cnt):
    global min_cut

    if cnt >= min_cut: # 백트래킹
        return

    cross_line = set()

    for i in range(N): # 잘리지 않은 전기줄에 대해 교차된게 없는지
        if cut[i]:
            continue

        if is_cross(i):
            cross_line.add(i)

    if not cross_line: # 교차된게 없으면
        min_cut = min(min_cut, cnt)
        return

    for line in cross_line: # 교차된것 중에 하나 자르기
        cut[line] = 1
        cut_line(cnt + 1)
        cut[line] = 0


cut_line(0)

print(min_cut)

