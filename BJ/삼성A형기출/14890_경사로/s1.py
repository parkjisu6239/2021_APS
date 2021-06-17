import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

N, L = q()
arr = [list(q()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

# 다음칸이랑 높이가 같으면 전진 가능
# 다음칸이랑 높이가 +- 1차이가 나고, 다음칸 = 다담칸이랑, 경사로 미설치 인경우 전진 가능


def go_R(R, idx, sign):

    if (sign == 1 and idx == N-1) or (sign == -1 and idx == 0):
        return True

    if arr[R][idx] == arr[R][idx+1*sign]:
        return go_R(R, idx+1*sign, sign)

    elif abs(arr[R][idx] - arr[R][idx+1*sign]) > 2:
        return False # 차이가 2 이상이면 종료

    else: # 차이가 1
        if visit[R][idx+1*sign]: return False

        for k in range(1, L):
            if idx+(1+k)*sign < N and arr[R][idx+1*sign] == arr[R][idx+(1+k)*sign] and visit[R][idx+(1+k)*sign] == 0:
                continue
            else:
                return False

        for k in range(L):
            visit[R][idx + (1 + k) * sign] = 1

        return go_R(R, idx+L*sign, sign)

def go_C(C, idx, sign):

    if (sign == 1 and idx == N-1) or (sign == -1 and idx == 0):
        return True

    if arr[idx][C] == arr[idx+1*sign][C]:
        return go_C(C, idx+1*sign, sign)

    elif abs(arr[idx][C] - arr[idx+1*sign][C]) > 2:
        return False # 차이가 2 이상이면 종료

    else: # 차이가 1
        if visit[idx+1*sign][C]: return False

        for k in range(1, L):
            if idx+(1+k)*sign < N and arr[idx+1*sign][C] == arr[idx+(1+k)*sign][C] and visit[idx+(1+k)*sign][C] == 0:
                continue
            else:
                return False

        for k in range(L):
            visit[idx + (1 + k) * sign][C] = 1

        return go_C(C, idx+L*sign, sign)


# result = 0
# for i in range(N):
#     if go_R(i, 0, 1) and go_R(i, N-1, -1):
#         print(i)
#         result += 1
#     if go_C(i, 0, 1) and go_C(i, N-1, -1):
#         print(i)
#         result += 1
#
# print(result)

print(go_C(0, N-1, -1))