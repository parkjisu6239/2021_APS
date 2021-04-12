# 짝수 = 짝수 + 짝수 > 이경우는 4 = 2+2 인 경우만 되고 6이상은 안된다(2가 아닌 짝수는 소수가 아님)
# 짝수 = 3이상의 홀수 + 3이상의 홀수
# 4이면 1, 그 이상의 짝수는 3이이상의 홀수 중에서 소수를 판단해야한다.

# 3이상의 홀수 + 3이상의 홀수 조합을 찾자


def prime(N):
    result = 0
    if N == 4:
        return 1

    for i in range(3, N // 2 + 1, 2):
        flag1 = 1
        for i_prime in range(3, int(i ** 0.5) + 1, 2):
            if i % i_prime == 0:
                flag1 = 0
                break
        flag2 = 1
        for N_i_prime in range(3, int((N - i) ** 0.5) + 1, 2):
            if (N - i) % N_i_prime == 0:
                flag2 = 0
                break

        if flag1 and flag2:
            result += 1

    return result

N = 6
for _ in range(1):
    #N = int(input())

    print(prime(N))