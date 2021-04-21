def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)


def solution(n, k):
    # k번째를 구하는 거라서, 처음부터 구할 필요가 없음!
    # 첫번째 원소를 고정했을때, 남은 수들로 만들어지는 경우의 수는 (n-1)!
    result = []
    nums = list(range(1, n+1))

    i = 1
    while True:
        facto = factorial(n - i)

        fix, k = divmod(k, facto)
        if k == 0:
            result.append(nums.pop(fix - 1))
            if fix:
                result += nums[::-1]
            else:
                result += nums
            break
        else:
            result.append(nums.pop(fix))

        i += 1

    return result


print(solution(3, 5))


