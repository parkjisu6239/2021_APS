import sys
sys.stdin = open("input.txt", "r")

def dump(N, boxes):
    # 주어진 덤프횟수만큼 실행
    for _ in range(N):
        #find min,max
        min_idx = max_idx = 0
        for idx in range(len(boxes)):
            if boxes[max_idx] < boxes[idx]:
                max_idx = idx
            if boxes[min_idx] > boxes[idx]:
                min_idx = idx

        # dump
        if boxes[max_idx] - boxes[min_idx] <= 1:
            return boxes[max_idx] - boxes[min_idx]
        else:
            boxes[max_idx] -= 1
            boxes[min_idx] += 1

    # dump가 완료된 상태의 최대-최소가 출력해야하는 값이기때문에
    # 덤프 반복문 완료 후에 최대최소를 한번 더 구해야함
    min_idx = max_idx = 0
    for idx in range(len(boxes)):
        if boxes[max_idx] < boxes[idx]:
            max_idx = idx
        if boxes[min_idx] > boxes[idx]:
            min_idx = idx

    return boxes[max_idx] - boxes[min_idx]



for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, dump(N, boxes)))