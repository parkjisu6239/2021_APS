def solution(n):
    # 목표 N이 홀수라면 -1 하고 //2, 짝수라면 //2를 반복하고 홀수라면 -1한 횟수세기
    result = 0
    while n > 0:
        if n % 2:
            n -= 1
            n //= 2
            result += 1
        else:
            n //= 2

    return result

print(solution(5000))