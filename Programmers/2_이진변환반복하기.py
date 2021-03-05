def solution(s):
    change = 0
    remove_zero = 0

    while s != '1':
        # 제거할 0의 개수를 센다
        temp_remove_zero = 0
        for i in range(len(s)):
            if s[i] == '0':
                temp_remove_zero += 1
        # 제거한 0의 개수를 더한다.
        remove_zero += temp_remove_zero
        # 0을 제거한 문자열의 길이를 N으로 저장한다.
        N = len(s) - temp_remove_zero

        # N을 이진수로 변환한다.
        s = ''
        while N > 0:
            s = str(N % 2) + s
            N //= 2

        # 이진 변환 횟수 증가
        change += 1

    return [change, remove_zero]

print(solution("110010101001"))