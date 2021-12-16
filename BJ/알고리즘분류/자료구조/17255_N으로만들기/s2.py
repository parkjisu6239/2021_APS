import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

target = input()
result = 0


def dfs(s):
    global result

    if len(s) == 1:
        result += 1
        return

    L = set(list(s))
    if len(L) == 1:
        result += 1
        return

    dfs(s[1:])
    dfs(s[:-1])


dfs(target)
print(result)
