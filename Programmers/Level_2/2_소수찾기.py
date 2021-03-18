from itertools import permutations

def solution(numbers):
    # 일단 부분집합을 구한다
    # 부분집합 원소들에 대해 소수 검사를 한다 !> 부분집합이 아니라 순열을 만들어야한다
    # 포인트 011을 정수로 어떻게 바꿀것인가? > int를 쓰니까 자동으로 된다^^
    answer = 0
    numbers = list(numbers)
    all_number = []
    for i in range(1, len(numbers) + 1):
        all_number.extend(list(map(int, map(''.join, permutations(numbers, i)))))
    all_number = list(set(all_number))

    print(all_number)
    for sub in all_number:
        if sub == 0 or sub == 1 or (sub != 2 and sub % 2 == 0): # 1이거나 2가 아닌 짝수이면 소수X
            continue
        if sub == 2: # 2도 소수니까 빠르게 확인
            answer += 1
            continue

        for i in range(2, round(sub**0.5)+1): # 1이 아닌 약수를 찾기 위해 2부터 round(sub**0.5)까지
            if sub % i == 0:
                break # 나누어 떨어지면 약수있는거니까 검사그만!
        else: # break 안걸리고, 다 검사해서 나온거면 약수없는 것 = 소수
            answer += 1
    return answer


print(solution("011"))


