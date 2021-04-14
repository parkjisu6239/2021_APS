import sys
import time
sys.stdin = open('input.txt')
start = time.time()

for tc in range(1, int(input())+1):
    nums, swap = map(str, input().split())
    nums = list(nums)
    swap = int(swap)

    # 최대인지 확인하기 위한 변수
    DECS = sorted(nums, reverse=True)

    # 32888을 최대로 바꾸기 위해서는 88832 이어야 하는데
    # 아래 while 문만 마치면 88823가 된다.
    # 그래서 같은 숫자랑 swap이 된 경우 추가적인 처리를 하기 위한 변수이다.
    # changed_nums[숫자] : swap이 일어난 경우 '숫자'가 원래있던 위치
    # ex) changed_nums[8] = [4, 3]
    changed_nums = [[] for _ in range(10)]

    idx = 0
    n = len(nums)
    while swap > 0:
        # 최대라면 교체 그만
        if nums == DECS:
            break

        # 선택 정렬 형태와 유사
        max_idx = idx
        for i in range(idx+1, n):
            if nums[i] >= nums[max_idx]:
                max_idx = i

        if nums[idx] != nums[max_idx]:
            changed_nums[int(nums[max_idx])].append(max_idx)
            nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
            swap -= 1

        idx += 1

    # swap 횟수가 남은 경우 (nums == DECS 이라서 break된 경우)
    if swap:
        # 남은 swap은 무조건 써야함
        # swap이 짝수번 남은 경우에는 그냥 원래대로 돌리는게 가능하니까 그대로 둬도 됨
        # swap이 홀수번 남은 경우엔, 마지막 1번은 어찌됐든 해야함
        # 근데 만약 중복된 값이 있으면(75270) 그 똑같은 둘이 바꾸면 되니까 역시 변화 X
        if len(nums) == len(set(nums)) and swap%2:
            # 근데 swap이 홀수고, 중복이 하나도 없으면 어쩔수 없이 바꿔야만 함
            # 근데 이왕 바꿔야하면 제일 작은 값 두개를 바꾸는게 그나마 최대임
            nums[-1], nums[-2] = nums[-2], nums[-1]
    # swap이 0인 경우
    else:
        for changed_num in changed_nums:
            # 만약 중복값이 있어서 같은 숫자를 여러번 바꾼 경우 ex) changed_nums[8] = [4, 3]
            if changed_num:
                # changed_nums[8] = [3, 4] 앞쪽에 큰거 둬야 되고 인덱스는 앞>뒤로 볼꺼라 sort함
                changed_num.sort()
                # 위에 했던거랑 동일
                for i in range(len(changed_num)-1):
                    local_max_idx = i
                    for j in range(i+1, len(changed_num)):
                        if nums[changed_num[j]] >= nums[changed_num[local_max_idx]]:
                            local_max_idx = j
                    nums[changed_num[i]], nums[changed_num[local_max_idx]] = nums[changed_num[local_max_idx]], nums[changed_num[i]]

    print('#{} {}'.format(tc, int(''.join(nums))))

print(time.time() - start) # 0.0009982585906982422
