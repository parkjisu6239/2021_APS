import sys
import time
sys.stdin = open('input.txt')
start = time.time()

def solution(swap):
    global result
    # 모든 교환이 끝난 경우
    if swap == 0:
        # 최대값인 경우 갱신
        if int(''.join(nums)) > result:
            result = int(''.join(nums))
        return

    # 교환
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            temp = ''.join(nums)
            # 나온적 없는 결과일 경우
            if (temp, swap) not in visit:
                # 추가, 재귀 호출
                visit.add((temp, swap))
                solution(swap-1)
            # 재귀호출이 종료되었거나, 같은 결과가 있는 경우엔 원상복구
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, int(input())+1):
    nums, swap = map(str, input().split())
    nums = list(nums)
    swap = int(swap)
    result = 0
    visit = set()
    solution(swap)
    if result == 0:
        result = int(''.join(nums))
    print('#{} {}'.format(tc, result))

print(time.time() - start) # 0.0009996891021728516
