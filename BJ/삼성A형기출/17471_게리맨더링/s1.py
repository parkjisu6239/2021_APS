import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))
tree = [[] for _ in range(N)]
for n in range(N):
    cnt, *nodes = map(int, input().split())
    for node in nodes:
        tree[n].append(node-1)


def check_connect(nodes):
    q = [nodes[0]]
    visit = [0]*N
    visit[nodes[0]] = 1
    connects = 0
    people = 0

    while q:
        v = q.pop(0)
        connects += 1
        people += value[v]
        for w in tree[v]:
            if w in nodes and visit[w] == 0:
                visit[w] = 1
                q.append(w)

    if connects == len(nodes):
        return people
    else:
        return 0


def solution():
    ans = 987654
    for i in range(1, (1 << N) -1):
        A, B = [], []
        for n in range(N):
            if i & (1 << n):
                A.append(n)
            else:
                B.append(n)

        a = check_connect(A)
        b = check_connect(B)
        if a and b:
            ans = min(ans, abs(a - b))

    return -1 if ans == 987654 else ans


print(solution())
