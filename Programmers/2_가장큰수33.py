def solution(numbers):
    N = len(numbers)
    sel = [0] * N
    visit = [0] * N
    max_num = 0

    def perm(idx):
        nonlocal max_num
        if idx == N:
            s = ''.join(map(str, sel))
            if int(s) > max_num:
                max_num = int(s)
            return

        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                sel[idx] = numbers[i]
                perm(idx + 1)
                visit[i] = 0

    perm(0)

    return str(max_num)