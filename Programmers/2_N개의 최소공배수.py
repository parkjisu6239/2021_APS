def solution(arr):
    # 한개 잡아서 그 숫자의 배수가 다른 모든 숫자들에 의해
    # 나누어 떨어진다면, 그게 최소 공배수
    # 가장 큰 수로하면 반복 횟수를 줄일 수 있다.
    # 실제로 sort하면 최대 55ms, 안하면 164ms가 나옴.
    LCM = arr[-1]
    k = 1
    while True:
        for i in range(len(arr) - 1):
            if k * LCM % arr[i]: break
        else:
            break
        k += 1

    return k * LCM