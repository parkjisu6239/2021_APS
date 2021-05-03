# 그 풍선이 남으려면, 그 풍선 기준으로 왼쪽들의 최소값, 오른쪽들의 최소값을 구한후
# 양쪽 적어도 최소값들 중 하나보다 커야한다.
# ~~~~ 4 ~~~~~ 이런 경우 여차저차 하여 (모두 큰것들만 터뜨린 경우)
# leftmin 4 rightmin 이 될 것이다. 이때 4가 남기 위해서는 (leftmin 4 rightmin) 중에서 4가 최소이거나,
# leftmin < 4 < rightmin 이여서 rightmin 터치고, 한번은 작은거 터쳐도 되니 leftmin 터쳐서 4를 남긴다.
# 혹은 leftmin > 4 > rightmin 이여야 한다.
# 단 4 > leftmin and 4 > rightmin 이면 안된다.
# min으로 했더니 시간초과 ^^

# def solution(a):
#     result = 0
#     for i in range(1, len(a) - 1):
#         Lmin = min(a[:i])
#         Rmin = min(a[i + 1:])
#         if a[i] < Lmin or a[i] < Rmin:
#             result += 1
#     return result + 2

def solution(a):
    result = 0
    # 양쪽 최소값 한번에 찾기 위해 리스트 구성
    LRmin = [[0, 0] for _ in range(len(a))]

    # 왼쪽최소, 오른쪽최소는 양끝값으로 초기화
    Lmin = a[0]
    Rmin = a[-1]

    for i in range(1, len(a) - 1):
        LRmin[i][0] = Lmin # 1번부터 뒤로가면서 왼쪽 최솟값 찾기
        LRmin[len(a)-1-i][1] = Rmin # -2부터 뒤로 가면서 오른쪽 최솟값 찾기

        if a[i] < Lmin: # 더 작은값이 나오면 왼쪽 최소 갱신
            Lmin = a[i]

        if a[len(a)-1-i] < Rmin: # 더 작은 값이 나오면 오른쪽 최소 갱신
            Rmin = a[len(a)-1-i]

    for i in range(1, len(a) - 1):
        if a[i] < LRmin[i][0] or a[i] < LRmin[i][1]:
            result += 1

    return result + 2 # 앞뒤는 무조건 포함

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))