import sys
sys.stdin = open('input.txt')

def FindMatrix(container):
    ans = []

    for i in range(n):
        for j in range(n):
            # 처음 0이아닌 값이 나왔다면
            if container[i][j]:
                r_size , c_size = 0, 0
                for r in range(n - i):
                    if container[i+r][j]:
                        r_size += 1
                    else: break
                for c in range(n-j):
                    if container[i][j+c]:
                        c_size += 1
                    else: break

                # 사이즈 순으로 정렬해야 되서 사이즈도 넣어줌
                ans.append([r_size*c_size, r_size, c_size])

                # 이미 확인한 행렬을 0으로 만들어서 바꿔줌
                for k in range(r_size):
                    for l in range(c_size):
                        container[i+k][j+l] = 0

    # sorted....
    return sorted(ans)


for tc in range(1, int(input())+1):
    n = int(input())
    container = [ list(map(int, input().split())) for _ in range(n)]

    # 출력 주의!
    # 출력은 행렬의 갯수, 서로 다른 용기(?) 의 행과 열 크기 출력 행열크기는 크기 오름차순
    result = FindMatrix(container)

    N = len(result)
    print('#{} {}'.format(tc, N), end = " ")

    for i in range(N):
        print(result[i][1], result[i][2], end=" ")
    print()
