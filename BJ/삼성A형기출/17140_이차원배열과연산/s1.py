import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

r, c, k = q()
arr = [[0]*100 for _ in range(100)]

for i in range(3):
    temp = list(q())
    for j in range(3):
        arr[i][j] = temp[j]

R, C = 3, 3

def solution():
    ans = 0
    while arr[r-1][c-1] != k:
        calculation(R, C)
        ans += 1
        if ans > 100:
            return -1

    return ans


def calculation(R, C):
    if R >= C: # R 연산
        sort_R()
    else: # C 연산
        sort_C()


def sort_R():
    global R, C

    max_m = 0
    for i in range(R):
        # 카운팅
        count = dict()
        for j in range(C):
            if arr[i][j] == 0:
                continue
            count[arr[i][j]] = count.get(arr[i][j], 0) + 1

        # 정렬
        sorted_count = sorted(count.items(), key=(lambda x: x[1]))
        m = 0
        for num, cnt in sorted_count:
            arr[i][m], arr[i][m + 1] = num, cnt
            m += 2
            if m >= 100:
                break
        max_m = max(max_m, m)
        for l in range(m, 100):
            if arr[i][l]:
                arr[i][l] = 0
            else:
                break
    C = max_m


def sort_C():
    global R, C

    max_m = 0
    for j in range(C):
        # 카운팅
        count = dict()
        for i in range(R):
            if arr[i][j] == 0:
                continue
            count[arr[i][j]] = count.get(arr[i][j], 0) + 1

        # 정렬
        sorted_count = sorted(count.items(), key=(lambda x: x[1]))
        m = 0
        for num, cnt in sorted_count:
            arr[m][j], arr[m + 1][j] = num, cnt
            m += 2
            if m >= 100:
                break
        max_m = max(max_m, m)
        for l in range(m, 100):
            if arr[l][j]:
                arr[l][j] = 0
            else:
                break

    R = max_m

print(solution())



