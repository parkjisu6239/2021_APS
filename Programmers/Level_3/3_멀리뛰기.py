def solution(n):
    # 수영장 문제랑 같음

    answer = 0

    def jump(kan):
        nonlocal answer

        if kan == n:
            answer += 1
            answer %= 1234567
            return

        if kan > n:
            return

        jump(kan + 1)
        jump(kan + 2)

    jump(0)

    return answer % 1234567


def solution(n):
    # 수영장 문제랑 같은 줄 알았으나 피보나치 느낌

    # n일때 횟수는 n-1에서 한칸 뛴거랑, n-2에서 두칸 뛴거랑 같다.
    # n=1 => result=1
    # n=2 => result=2
    # n=3 => result=3
    # n=4 => result=5

    jump = [1, 2]

    if n < 3:
        return jump[n - 1] % 1234567

    for _ in range(n - 2):
        jump.append(jump[-1] + jump[-2])

    return jump[n - 1] % 1234567