import sys
from functools import cmp_to_key

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
_arr = [input().rstrip() for _ in range(n)]
alpha = {}

no = 0
for i in range(65, 91):
    alpha[chr(i)] = no
    alpha[chr(i + 32)] = no + 1
    no += 2


def processed_arr(arr):
    result = []
    for str in arr:
        temp = []
        num = ""
        for s in str:
            if s.isdigit():  # number
                num += s
                continue
            elif num:
                temp.append(num)
                num = ""
            temp.append(s)
        if num:
            temp.append(num)
        result.append([str, temp])
    return result


def who_is_first(first, second):
    for i in range(min(len(first[1]), len(second[1]))):
        if first[1][i] == second[1][i]:  # 같으면 다음
            continue
        if first[1][i].isdigit() and second[1][i].isdigit(): # 둘다 숫자
            if int(first[1][i]) == int(second[1][i]): # int가 같은 경우
                if len(first[1][i]) == len(second[1][i]): # 길이도 같으면 다음 비교
                    continue
                return len(first[1][i]) - len(second[1][i]) # 짧은게 더 앞
            else: # int가 다른 경우
                return int(first[1][i]) - int(second[1][i]) # 작은 수가 더 앞
        elif first[1][i].isalpha() and second[1][i].isalpha(): # 둘다 문자
            return alpha[first[1][i]] - alpha[second[1][i]] # AaBb 순서
        else:
            return -1 if first[1][i].isdigit() else 1

    return len(first[1]) - len(second[1])


arr = processed_arr(_arr)

print(arr)
answer = sorted(arr, key = cmp_to_key(who_is_first))

for a, b in answer:
    print(a)
