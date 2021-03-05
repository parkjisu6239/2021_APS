def solution(n):
    # 재귀로 하면 시간초과 되서 리스트로
    fibo = [0, 1]
    for i in range(n - 1):
        fibo.append(fibo[-1] + fibo[-2])

    return fibo[-1] % 1234567

print(solution(3))