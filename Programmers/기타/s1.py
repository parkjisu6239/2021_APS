def solution(a, b):
    value = 1
    ans = [-1] * b
    pattern = dict()
    start = 0
    end = 0
    for i in range(b):
        value *= a
        if value > 99999:
            value %= 100000

        if pattern.get(value, -1) != -1:
            start = pattern[value]
            end = i
            break

        ans[i] = value
        pattern[value] = i
    else:
        return ans[b-1]

    idx = start + (b-start)%(end-start)
    if start == 0:
        idx -= 1

    return ans[idx]


print(solution(123456789, 12345))
print(solution(5, 14))
print(solution(2, 26))