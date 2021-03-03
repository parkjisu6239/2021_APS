import sys
sys.stdin = open("input.txt", "r")
'''
# min max 사용
for tc in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))

    dump_cnt = 0
    while dump_cnt < N:
        if max(box_list) - min(box_list) <= 1:
            break
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1
        dump_cnt += 1

    print('#{} {}'.format(tc, max(box_list) - min(box_list)))


# min max 미사용
for tc in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))

    dump_cnt = 0

    while dump_cnt <= N:
        max_box = min_box = box_list[0]
        max_box_idx = min_box_idx = 0

        for i in range(len(box_list)):
            if box_list[i] > max_box:
                max_box = box_list[i]
                max_box_idx = i
            if box_list[i] < min_box:
                min_box = box_list[i]
                min_box_idx = i

        if max_box - min_box <= 1:
            break

        box_list[max_box_idx] -= 1
        box_list[min_box_idx] += 1
        dump_cnt += 1

    print('#{} {}'.format(tc, max_box - min_box))

'''
# 교수님 코드
def flatten(dump_limit, boxes):
    for _ in range(dump_limit):
        # 최대, 최소를 찾기 위한 인덱스 초기화
        max_idx = min_idx = 0
        # 최대와 최소를 찾아보자
        # 박스 리스트의 크기만큼 반복을 돌면서
        for i in range(1, len(boxes)):
            # 만약 현재 인덱스의 상자 높이가 최댓값보다 크면
            if boxes[i] > boxes[max_idx]:
                # max_idx(우리가 실제 원하는 값은 value)
                max_idx = i
            if boxes[i] < boxes[min_idx]:
                # min_idx(우리가 실제 원하는 값은 value)
                min_idx = i

        # 박스 전달 (최대 > 최소)
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 평탄화가 완료되었다면? 더이상 평탄화 할 필요 없음!
        if boxes[max_idx] == boxes[min_idx]:
            return 0
        elif (boxes[max_idx] - boxes[min_idx]) == 1:
            return 1

    # 제한된 횟수의 덤프 작업이 끝나면
    max_val = min_val = boxes[0]
    for i in range(1, len(boxes)):
        if boxes[i] > max_val:
            max_val = boxes[i]
        if boxes[i] < min_val:
            min_val = boxes[i]

    ans = max_val - min_val

    return ans

for tc in range(1, 11):
    # 덤프 횟수
    dump_limit = int(input())
    # 상자 리스트
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, flatten(dump_limit, boxes)))