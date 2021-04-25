
N = 36

def solution(N):
    l = 1
    r = N

    while l <= r:
        m = (l + r) // 2
        M = m*m

        if M == N:
            return m
        elif M < N: # 큰걸 찾으러 가야함
            l = m + 1
        else: # 작은걸 찾으러 가야함
            r = m - 1

print(solution(N))
