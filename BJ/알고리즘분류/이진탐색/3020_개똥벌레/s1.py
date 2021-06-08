import sys
sys.stdin = open('eval_input.txt')

N, H = map(int, input().split())
cave = [int(input()) for _ in range(N)]
# 짝수인덱스:종유석, 홀수인덱스:석순

left = 0 # 바닥으로 갈 경우
right = H-1 # 맨위로 갈 경우
result = []
cnt = 0

def Distroy(hight):
    distroy = 0
    for i in range(len(cave)):
        if i % 2 == 0 and cave[i] > hight: # 짝수
            distroy += 1
        elif i % 2 == 1 and H - cave[i] <= hight: # 홀수
            distroy += 1

    return distroy

def BinarySearch(left, right):
    global result
    if left > right:
        return
    mid = (left + right) // 2

    dis_cnt = Distroy(mid)

    result.append(dis_cnt)

    BinarySearch(left, mid-1)
    BinarySearch(mid+1, right)


BinarySearch(left, right)

answer = min(result)
print(result, answer, result.count(answer))






