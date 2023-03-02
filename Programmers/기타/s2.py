def solution(a, b):
    value = 1
    ans = []
    start = 0
    for _ in range(b):
        value *= a
        if value > 99999:
            value %= 100000

        if value in ans:
            start = ans.index(value)
            break

        ans.append(value)
    else:
        return ans[b-1]

    idx = start + (b-start)%(len(ans)-start)
    if start == 0:
        idx -= 1

    print(ans[:10])

    return ans[idx]

print(solution(123456789, 12345))
print(solution(5, 14))
print(solution(2, 26))