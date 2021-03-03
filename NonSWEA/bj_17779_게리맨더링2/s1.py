import sys
from pandas import DataFrame as df
sys.stdin = open("input.txt")

N = int(input())
# 재현시 사람들
JaeHyun = [ list(map(int, input().split())) for _ in range(N)]


# 선거구를 나누는 방법이 많다! 가능한 기준점, 경계의 길이가 1개 이상이다.
# 선거구를 나누를 여러방법에서 각각 최대최소를 구하고, 그 중에서 최소값을 찾아야한다.
# 선거구를 나누는 방법의 개수만큼 선거구를 만들어내야 하나??

# 기준점 2차원배열의 가장자리일수 있는가?
# y는 1일 수 없다. d1 >= 1 이기때문에, 1 ≤ y-d1 를 만족하여면 y는 d1보다 커야한다.
# (1,2) 일 경우 d1 = 1
# 직관적으로 생각하면, 기준점과 경계의 길이는 마름모를 만들 수 있느냐!
# 그리고, 마름모는 N*N을 넘을 수 없다! 정도로 생각 할 수 있다.

# 기준점
people = [0, 0, 0, 0, 0]
for x in range(N-1):
    for y in range(1,N-1):
        # 선거구 초기화
        ward = [[0 for _ in range(N)] for _ in range(N)]
        for d1 in range(1,N):
            for d2 in range(1, N):
                if d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                    print(x, y, d1, d2)
                    if d1 > d2:
                        # 5번 선거구 지정
                        for i in range(d2+1):
                            for j in range(i*2 + 1):
                                ward[x+i][y-i+j] = 5
                        for i in range(d2+1):
                            for j in range(i*2 + 1):
                                ward[x+d2+d1-i][y-i+j] = 5

                        # 1번 선거구 지정
                        for i in range(x+d1):
                            for j in range(y+1):
                                if ward[i][j] == 0:
                                    ward[i][j] = 1

                        # 2번 선거구 지정
                        for i in range(x+d2):
                            for j in range(y+1, N):
                                if ward[i][j] == 0:
                                    ward[i][j] = 2

                        # 3번 선거구
                        for i in range(x+d1, N):
                            for j in range(y):
                                if ward[i][j] == 0:
                                    ward[i][j] = 3

                        # 4번 선거구
                        for i in range(x+d2, N):
                            for j in range(y+1, N):
                                if ward[i][j] == 0:
                                    ward[i][j] = 2





# 예제 1의 경우만 봐도 선거구를 나누는 방법이 80개나 된다
# 이걸 다봐야할까?
