A, B = [1, 4, 2], [5, 4, 4]
N = len(A)
visit = [0] * N
sel = [0] * N

min_total, total = 99999999, 0

def perm(idx):
    global min_total, total

    if idx == N:
        if total < min_total:
            min_total = total
        return

    if total > min_total: return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            sel[idx] = i
            total += A[idx] * B[i]

            perm(idx + 1)
            visit[i] = 0
            total -= A[idx] * B[i]

perm(0)
print(min_total)
