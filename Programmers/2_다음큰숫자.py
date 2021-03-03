def solution(n):
    # while문으로 찾을때까지 반복하고, 찾으면 종료되게끔 구현하자
    # +1씩 하면서 비트 연산자로 1의 개수가 같은지 알아보자?
    # 느리지만 정확한건 1씩 더하고, 2로 나누면서 1갯수 세기
    answer = 0
    n_duple = n
    n_1_cnt = 0
    while n_duple > 0:
        if n_duple % 2:
            n_1_cnt += 1
        n_duple //= 2

    k = 1
    while True:
        test = n + k
        test_duple = test
        test_1_cnt = 0

        while test_duple > 0:
            if test_duple % 2:
                test_1_cnt += 1
            test_duple //= 2


        if test_1_cnt == n_1_cnt:
            return test

        k += 1

print(solution(78))