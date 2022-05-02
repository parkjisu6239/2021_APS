import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
value = input().rstrip()

# 1. 문자열 전체를 봄
# 2.1 팰린드롬인경우 - 모든 문자가 같으면 -> -1
# 2.2 아니면 길이 - 1
# 3. 팰린드롬이 아닌 경우 -> 길이를 반환


def is_palindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str) -1 - i]:
            return False
    return True


def solution(value):
    if len(set(value)) == 1:
        return -1

    if not is_palindrome(value):
        return len(value)

    return len(value) - 1


print(solution(value))