def solution(number, k):
    # <idea> N = len(number), M = N - k 라고 하면, 만들어야 되는 수는 M자리의 수
    # 1. 그러면 일단 N의 제일 왼쪽(앞쪽)에 올 숫자는 최대값이어야 함. 단, 구간은 0~N-M 까지
    # 2. 이때 최대값의 인덱스보다 작은 인덱스 값을 버리고 최대값의 인덱스부터 다시 찾기 시작 > 이때 버린게 l개 이라고 하자
    # 이제 버려야할 갯수는 k-l개. 맨앞말고 그 뒤중에서 최대값을 구함.
    # 그 최대값 인덱스랑 0이랑 차이가 k-l보다 작으면 그 사이의것 들을 버림
    # 차이가 크면, 그다음 최대값을 찾아서 같은 확인을 해봄
    # 언제까지? 제거한 숫자가 k가 될때까지

    # 안되는 테케 발견! solution("1212121", 6) > 기대값 2
    # k가 1인 경우 or 자리수보다 1작은 경우 반복문 수행 필요 없이 바로 끝날 수 있게!
    if len(number) - 1 == k:
        return str(max(list(map(int, number))))
    elif k == 1:
        number.replace(str(min(list(map(int, number)))), "")
        return number

    # 시작!
    # 1. 자리수만큼의 구간내에서 최대값을 찾는다.
    N = len(number)
    M = N - k
    max_idx = 0
    for i in range(N - M + 1):
        if int(number[i]) > int(number[max_idx]):
            max_idx = i

    # 2. 최대값보다 전에 있는 값은 제거하고, 내가 제거한 숫자의 개수에 더한다.
    remove_count = max_idx - 0
    number = number[max_idx:]

    # 3.
    fix = 1
    while remove_count < k:
        # 맨앞을 제외한 값중 최대값을 구함, 맨앞은 고정되었으니까!
        # fix는 내가 고정한 갯수, 앞에서 확정된 숫자 다음부터 최대값을 구해야하기 때문
        max_idx = fix
        # 확정값 다음부터, 내가 뺄수 있는개수+1까지 중에서 최대값을 찾음
        # 그 밖에서 최대값 구해봤자 제거할수 있는 개수를 넘어가서 그걸 붙여 쓸수 없음
        for i in range(fix, fix + k-remove_count + 1):
            if int(number[i]) > int(number[max_idx]):
                max_idx = i
        # 최대인덱스를 구한 후, 그 사이에 있는건 빼버리자
        # 제거한 개수도 늘려주고, 확정된 값도 하나 늘었으니, 늘려주자
        number = number[:fix] + number[max_idx:]
        remove_count += max_idx - fix
        fix += 1

        # 안되는 테케 발견! solution("987654321", 4) 발견하고 아래 코드 추가해서 런타임에러 해결!
        # 근데 아직 2개가 시간초과!
        if fix == M:
            return number[:M]

    return number


print(solution("1212121", 6))
# 안되는 테케 발견! solution("987654321", 4)
# 안되는 테케 발견! solution("1212121", 6) > 기대값 2

# 위 두개 모두 처리 했지만, 프로그래머스 테케에서 2개가 시간초과 그대로;; 무지막지하게 큰 수가 들어오기 때문