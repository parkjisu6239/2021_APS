import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_cut_vertex(node):
    if adj[node] > 1:
        return "yes"
    return "no"


N = int(input())
adj = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a] += 1
    adj[b] += 1


M = int(input())
for __ in range(M):
    t, k = map(int, input().split())
    if t == 1:
        print(is_cut_vertex(k))
    elif t == 2:
        print("yes")