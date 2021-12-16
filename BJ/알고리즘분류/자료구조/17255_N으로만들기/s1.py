import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

target = input()
result = set()


def solution(num, start, end, stack):
    if num == target:
        result.add(''.join(stack))
        return

    if start == 0:
        solution(num + target[end+1], start, end + 1, stack + [num + target[end+1]])
    elif end == len(target) - 1:
        solution(target[start - 1] + num, start - 1, end, stack + [target[start - 1] + num])
    else:
        solution(num + target[end + 1], start, end + 1, stack + [num + target[end+1]])
        solution(target[start - 1] + num, start - 1, end, stack + [target[start - 1] + num])


for i, t in enumerate(target):
    solution(t, i, i, [t])

print(len(result),result)
