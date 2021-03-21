def solution(n):
    # n개의 원판이 있을 경우
    # 1. 가장큰 n번 원판을 3번봉으로 옮기기 위해, n-1개 원판을 모두 2번봉으로 옮긴다.
    # 2. n번 원판을 3번봉으로 옮긴다.
    # 3. 2번봉에 있는 n-1개의 원판을 3번으로 옮긴다\
    # 결국 n을 3번봉으로 보내려면, n-1은 2번 봉에 있어야한다 / n-1을 2번봉으로 보내려면, n-2는 3번 봉에 있어야한다. ...
    # n개가 있을때 보내고자하는 봉으로 보내려면 가장 작은 원반 부터 위 규칙에 따라 옮기면 된다.
    answer = []

    def hanoi(n, start, to, via):
        if n == 1:
            answer.append([start, to])

        else:
            hanoi(n - 1, start, via, to)
            answer.append([start, to])
            hanoi(n - 1, via, to, start)

    hanoi(n, 1, 3, 2)

    return answer

print(solution(4))

print([[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]])

