from itertools import combinations

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0

    return 1


def solution(nums):
    answer = 0

    for combi in map(list, combinations(nums, 3)):
        answer += isPrime(sum(combi))

    return answer

print(solution([1, 2, 3, 4]))