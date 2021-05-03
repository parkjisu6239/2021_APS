def solution(gems):
    C = {}
    for gem in gems:
        C[gem] = C.get(gem, 0) + 1

    s, e = 0, len(gems)-1
    while 1:
        if C[gems[e]] > 1:
            C[gems[e]] -= 1
            e -= 1
        elif C[gems[s]] > 1:
            C[gems[s]] -= 1
            s += 1
        else:
            break

    return [s+1, e+1]


print(solution(["a", "b", "c", "d"]))
print(solution(["a", "b", "a", "c", "b"]))
print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))