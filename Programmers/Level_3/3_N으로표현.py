def solution(N, number):
    # N을 2번~?번 써서 만들어보자
    # 12 = 5 + 5 ; 5 - 5 ; 5/5 ; 5*5 ; 55 2개로 만들 수 있는 경우의 수
    # 사칙연산으로 만들 수 있는 경우의 수 > 10,0,1,25 ; 숫자의 연속으로 만든 경우의 수 > 5, 55
    # 3개 쓴다면, 저기에 사칙연산한 모든 경우 + 555
    if N == number:
        return 1

    # 최대 2개로 구성된 조합
    combinations = [0, 1, 2 * N, N ** 2, N, 10 * N + N]
    cntinu = 10 * N + N
    cnt = 2

    while number not in combinations:
        if cnt > 8:
            return -1
        corrent = list(combinations)
        for i in range(len(corrent)):
            combinations.append(corrent[i] + N)
            combinations.append(corrent[i] * N)
            combinations.append(N - corrent[i])
            combinations.append(corrent[i] - N)
            combinations.append(corrent[i] // N)
            if corrent[i] != 0:
                combinations.append(N // corrent[i])

        cntinu = cntinu * 10 + N
        combinations.append(cntinu)
        cnt += 1

        combinations = list(set(combinations))

    return cnt


print(solution(4, 17))