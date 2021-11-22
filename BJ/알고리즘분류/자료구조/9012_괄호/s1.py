import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(ps):
    stack = []
    for x in ps:
        if x == '(':
            stack.append('(')
        else:
            if len(stack):
                stack.pop()
            else:
                return 'NO'

    if len(stack):
        return 'NO'
    else:
        return 'YES'


N = int(input())
for _ in range(N):
    ps = input().rstrip()
    print(solution(ps))