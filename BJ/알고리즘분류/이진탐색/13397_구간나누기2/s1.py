# 이분탐색의 타겟 = 구간의 점수
# 구간점수들이 타겟보다 작거나 같아야 한다.
#
# 구간의 시작을 고정하고 끝을 늘려가면서 탐색하다가,
# 구간 점수가 타겟보다 크면 [시작~(끝-1)]으로 구간을 종료한다.
#
# 새로운 구간은 위에서 구한 끝을 시작으로 정하고 같은 과정을 반복한다.


import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def get_section_cnt(target):
    section_max, section_min = arr[0], arr[0] # 첫 구간의 최대 최소
    section_cnt = 1

    for i in range(1, N):
        section_max = max(section_max, arr[i]) # 구간 최대값
        section_min = min(section_min, arr[i]) # 구간 최솟값
        if section_max - section_min > target: # 구간점수가 타겟보다 큰 경우 -> 구간을 그렇게 나눌 수 없음
            section_cnt += 1 # 구간 종료 -> 구간 수 + 1
            section_max = arr[i] # 새로운 구간의 시작점 i
            section_min = arr[i] # 최대 = 최소 = arr[i] (구간의 원소가 하나니까)

    return section_cnt # 구간점수가 target을 넘지 않게 나눈 구간의 수(마지막 구간은 넘기도 함)


def bs():
    s, e = 0, max(arr)
    result = 0
    while e >= s:
        m = (s + e) // 2
        if get_section_cnt(m) <= M:
            e = m - 1
            result = m
        else:
            s = m + 1
    return result

print(bs())