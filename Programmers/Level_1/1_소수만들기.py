from itertools import combinations

def solution(nums):
    answer = 0
    is_prime = [1] * 1001
    is_prime[0] = is_prime[0] = 0

    for i in range(2, 500):
        for j in range(2, 1001//i):
            is_prime[i*j] = 0

    for combi in map(list, combinations(nums, 3)):
        answer += is_prime[sum(combi)]

    return answer

print(solution([1, 2, 3, 4]))