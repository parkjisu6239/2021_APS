def solution(n):
    # swea 문제와 동일
    # n=1 : 1
    # n=2 : 2
    # n=3 : 3
    # n=4 : 5
    # s(n) = s(n-1) + s(n-2)
    # n의 경우의 수를 만들기 위해서는 n-1 경우의 수에다 '|'을 붙이거나, n-2 경우의 수에 '=' 붙이는것
    # DP로 접근
    # 맨마지막 출력에서만 나누면 시간초과가 된다. 숫자 자체가 커져서 그냥 더하기임에도 불구하고 연산속도가 더 걸려서 그런것 같다!
    answer = 0
    tile = [1, 2]
    if n < 3:
        return tile[n - 1] % 1000000007

    for _ in range(n - 2):
        tile.append((tile[-1] + tile[-2]) % 1000000007)

    return tile[n - 1]