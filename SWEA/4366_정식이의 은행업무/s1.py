import sys
sys.stdin = open('eval_input.txt')

def binary_to_decimal(num):
    result = 0
    n = len(num)
    for i in range(n):
        result += int(num[i])*(2**(n-i-1))

    return result

def Ternary_to_decimal(num):
    result = 0
    n = len(num)
    for i in range(n):
        result += int(num[i]) * (3 ** (n - i - 1))

    return result



def solution(two, three):
    # 2진수의 교환 인덱스
    for i in range(len(two)):
        # 바꿀 값 0 or 1
        for k in range(2):
            if two[i] != str(k):
                # 바꾸기
                change_two = two[:i] + str(k) + two[i + 1:]
                # 3진수의 교환 인덱스
                for j in range(len(three)):
                    for l in range(3):
                        if three[j] != str(l):
                            change_three = three[:j] + str(l) + three[j + 1:]
                            # 10진수 변환 값이 같으면
                            a = binary_to_decimal(change_two)
                            b = Ternary_to_decimal(change_three)
                            # int(change_two, 2) == int(change_three, 3)
                            if a == b:
                                return a



for tc in range(1, int(input())+1):
    two = input()
    three = input()
    print('#{} {}'.format(tc, solution(two, three)))