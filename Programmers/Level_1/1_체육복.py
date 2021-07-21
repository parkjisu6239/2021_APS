def solution(n, lost, reserve):
    count = 0
    # 체육복 잃어버렸지만 여분이 있는 사람 리스트
    who_lost = list(set(lost) - set(reserve))
    who_reserve = list(set(reserve) - set(lost))

    # 잃어버린사람이 여분 있는 사람한테 받을때마다 count + 1
    for num in lost:
        if num + 1 in who_reserve:
            who_reserve.remove(num + 1)
            count += 1
        elif num - 1 in who_reserve:
            who_reserve.remove(num - 1)
            count += 1
    return n - len(lost) + count