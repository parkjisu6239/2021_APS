import sys
sys.stdin = open('input.txt')

def find(x: int) -> int:
    if x != data[x]:
        data[x] = find(data[x])
    return data[x]


def union(a: int, b: int) -> None:
    root1 = find(a)
    root2 = find(b)
    data[root2] = root1


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    data = {key: key for key in range(m)}
    line = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        line.append((x, y, z))

    line.sort(key=lambda x: x[2])
    total = 0
    for a, b, weight in line:
        if find(a) != find(b):
            union(a, b)
        else:
            total += weight

    print(total)