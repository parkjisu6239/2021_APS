# boj 6416 트리인가
# 부모는 하나여야한다.
# 1 -> 2 라면 2 -> 1이 있으면 안된다.

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_tree(p, c):
    global parent
    if parent.get(c, 0): # 부모가 있으면
        return False

    if parent.get(p, 0) == c: # 쌍방향인지 확인
        return False

    parent[c] = p
    return True


tc = 1
this_tc_end = False
ans = True

while True:
    parent = {}
    while not this_tc_end:
        lines = input().split("  ")
        for line in lines:
            u, v = map(int, line.split())
            if u == v == 0:
                this_tc_end = True
                break
            if not is_tree(u, v):
                ans = False
                break

    if ans:
        print("Case " + str(tc) + " is a tree.")
    else:
        print("Case " + str(tc) + " is not a tree.")

    this_tc_end = False
    tc += 1
    if input().split():
        break

