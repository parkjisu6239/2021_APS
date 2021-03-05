# 순열
def perm(idx, numbers, sel, visit, max_num):
    if idx == len(numbers):
        s = ''.join(map(str, sel))
        max_num.append(int(s))
        return

    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = 1
            sel[idx] = numbers[i]
            perm(idx+1, numbers, sel, visit, max_num)
            visit[i] = 0


def solution(numbers):
    N = len(numbers)
    sel = [0] * N
    visit = [0] * N
    max_num = []

    perm(0, numbers, sel, visit, max_num)

    return str(max(max_num))

print(solution([3, 30, 34, 5, 9]))