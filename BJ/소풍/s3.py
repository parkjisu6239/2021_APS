# N, K, M = map(int, input().split())

N, K, M = 5, 2, 3
# (1) 2 3 4 5 > 1 (3) 4 5 > 1 3 (5) > (3) 5 > (3) > ''
# 탈락하는 사람 몇번째 사람? 2 > 3 > 1 > 2 > 1

cnt = 1
M -= 1
start = 0

while N > 0:
    out = (start + K-1) % N

    if out == M:
        break
    elif out < M:
        M -= 1

    start = out
    N -= 1
    cnt += 1


print(cnt)









