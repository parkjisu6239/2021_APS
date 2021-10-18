import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def select_area():
    total = all_people()
    ans = 987654321

    for x in range(1, N):
        for y in range(2, N):
            for d1 in range(1, y):
                for d2 in range(1, N-y+1):
                    if x + d1 + d2 <= N:
                        people = []
                        people.append(divide_area1(x, y, d1, d2))
                        people.append(divide_area2(x, y, d1, d2))
                        people.append(divide_area3(x, y, d1, d2))
                        people.append(divide_area4(x, y, d1, d2))
                        people.append(total - sum(people))
                        ans = min(ans, max(people) - min(people))

    return ans


def all_people():
    total = 0
    for i in range(N):
        for j in range(N):
            total += arr[i][j]
    return total


def divide_area1(x, y, d1, d2):
    total = 0
    k = 0
    for r in range(1, x + d1):
        if r >= x:
            k += 1
        for c in range(1, y-k+1):
            total += arr[r-1][c-1]

    return total


def divide_area2(x, y, d1, d2):
    total = 0
    k = 0
    for r in range(1, x + d2 + 1):
        if r > x:
            k += 1
        for c in range(y+1+k, N+1):
            total += arr[r - 1][c - 1]

    return total


def divide_area3(x, y, d1, d2):
    total = 0
    k = 1
    for r in range(x + d1, N + 1):
        for c in range(1, min(y - d1 - 1 + k, y - d1 + d2)):
            total += arr[r - 1][c - 1]
        if r <= x+d1+d2:
            k += 1

    return total


def divide_area4(x, y, d1, d2):
    total = 0
    k = 0
    for r in range(x + d2 + 1, N + 1):
        for c in range(max(y + d2 - k, y - d1 + d2), N + 1):
            total += arr[r - 1][c - 1]
        if r <= x+d1+d2:
            k += 1

    return total


print(select_area())


