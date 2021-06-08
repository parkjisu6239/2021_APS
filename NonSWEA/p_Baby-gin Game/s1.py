import sys
sys.stdin = open("eval_input.txt", "r")

def check_babygin(numbers):
    # numbers의 갯수를 셀 변수
    counter = [ 0 for _ in range(10)]

    is_babygin = 0

    # counter list 저장
    for number in numbers:
        counter[number] += 1

    # babygin을 판별
    #for idx in range(len(counter)):
    idx = 0
    while idx < len(counter):
        # triplet 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        # run 검증
        if idx < len(counter) - 2:
            # 연속된 3개의 숫자 확인(단축평가)
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue

        if is_babygin >= 2:
            return 1

        # while문의 idx를 올리는걸 하단에 두고,
        # 만약 위에 continue를 만나면, idx 더하지 않아서 같은 인덱스를 다시 확인함
        idx += 1
    return 0

# 입력받기
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input()))
    result = check_babygin(numbers)
    print('#{} {}'.format(tc,result))



'''
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input()))
    num_info = []
    # run과 triplet을 셀 변수
    cnt = 0
    # 0~9까지 숫자의 등장횟수를 num_info에 담음
    
    for i in range(10):
        num_info.append(numbers.count(i))
        # run 검사, 적어도 123부터 시작해서 i > 2
        if i > 2:
            # 연속된 세개 숫자의 갯수가 모두 1개 이상이면,
            if num_info[i] and num_info[i-1] and num_info[i-2]:
                # 카운트를 올리고, 각각 카운트를 1씩 내림
                cnt += 1
                num_info[i] -= 1
                num_info[i - 1] -= 1
                num_info[i - 2] -= 1

        # triplet 검사, 해당 숫자의 등장횟수가 3번 이상이면,
        if num_info[i] >= 3:
            cnt += 1
            num_info[i] -= 3

    # run or triplet 이 두개 이상이면,
    if cnt >= 2:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
'''