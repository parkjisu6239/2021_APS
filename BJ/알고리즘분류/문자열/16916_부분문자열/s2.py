import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

def Boier_mour(target, pattern):
    M = len(pattern)
    N = len(target)

    skip = dict()
    for i in range(len(pattern)):
        skip[pattern[i]] = len(pattern) -1 -i

    i = M-1 # target index
    j = M-1 # pattern index

    while j >= 0:
        while target[i] != pattern[j]: # 다르다면, 얼마나 스킵할지 구하기
            i += skip.get(target[i], M) # 해당 알파벳 인덱스의 값만큼 점프
            if i >= N: # 길이를 넘어가면, 탐색 실패
                return -1
            j = M - 1 # 다른 경우, i가 점프한 인덱스와 끝점 비교
        i -= 1
        j -= 1

    if i < -1:
        return 0

    return 1


target = input().rstrip()
pattern = input().rstrip()

print(Boier_mour(target, pattern))
