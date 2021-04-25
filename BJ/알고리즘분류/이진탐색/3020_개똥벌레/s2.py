import sys
sys.stdin = open('input.txt')

N, H = map(int, input().split())
top = []
bottom = []

for i in range(N):
    if i % 2 == 0:
        top.append(int(input()))
    else:
        bottom.append(int(input()))

top.sort()
bottom.sort()

result = []

for i in range(1, H+1):
    l, r = 0, len(bottom)-1
    bottom_cnt = 0
    while l <= r:
        mid = (l + r) // 2
        if bottom[mid] >= i: # 오름차순인데, 중간게 i보다 크거나 같으면
            bottom_cnt = len(bottom) - mid # 그다음에 있는건 일단 다 빠개고 가야됨
            r = mid - 1 # 부숴야 하는 시작점을 찾아야 되니까 왼쪽으로
        else:
            l = mid + 1


    l, r = 0, len(top) - 1
    top_cnt = 0
    while l <= r:
        mid = (l + r) // 2
        if H - top[mid] < i:  # 오름차순인데, 중간게 i보다 작으면
            top_cnt = len(top) - mid  # 그다음에 있는건 일단 다 빠개고 가야됨
            r = mid - 1
        else:
            l = mid + 1

    result.append(bottom_cnt+top_cnt)

answer = min(result)
print(answer, result.count(answer))







