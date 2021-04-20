import sys
sys.stdin = open('input.txt')

# 분할정복 & 백트래킹 #
# DP?로도 볼수 있을지? (작은 부분문제로 전체 문제 해결 가능)
# 2명 or 1명이 될때까지 작게 쪼개서, 해를 선택 -> 이 해들로 최종 해 도출 가능

def winner(a,b): # 정복
    if b == 0 or a[1] == b[1]:
        return a
    if a[1] == 1 :
        if b[1] == 2: return b
        else: return a
    elif a[1] == 2 :
        if b[1] == 3: return b
        else: return a
    elif a[1] == 3 :
        if b[1] == 1: return b
        else: return a


def solution(arr): # 분할
    if len(arr) == 2: # 길이가 2이면, 우승자 선택
        return winner(arr[0], arr[1])
    elif len(arr) == 1: # 길이가 1이면 부전승
        return arr[0]

    mid = (len(arr) + 1)//2 # 문제에서 주어진것으로 반반 나누기

    return winner(solution(arr[:mid]), solution(arr[mid:])) # 분할한다(정복도 같이 하긴 함)



for tc in range(1, int(input())+1):
    N = int(input())
    temp = list(map(int, input().split()))
    card = []
    for i in range(len(temp)):
        card.append([i+1, temp[i]])

    print('#{} {}'.format(tc, solution(card)[0]))

