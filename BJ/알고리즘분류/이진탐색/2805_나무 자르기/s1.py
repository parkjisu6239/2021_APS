import sys
sys.stdin = open('input.txt')

# input
N, M = map(int, input().split())
trees = list(map(int, input().split())) # 나무 최대 개수 100만

# 변수 정의
max_height = 1000000001 # 나무 최대 높이 10억
result = 0

# cut_height로 잘랐을 때 얻을 수 있는 나무 수를 구한다.
def GetTree(cut_height):
    cut_tree = 0

    for tree in trees:
        if tree > cut_height:
            cut_tree += tree - cut_height

    return cut_tree


# 절단기의 lowerbound 를 구하는 문제!
# 최소 어느 높이에서는 잘라야 M 이상 나무를 얻을 수 있다.
# cut_height↑  M↓, cut_height↓  M↑
def LowerBound(left, right): # 절단기 높이의 구간
    global result

    while left <= right: # 이진탐색 베이스 케이스와 동일
        mid = (left + right) // 2

        current_get_tree = GetTree(mid)

        if current_get_tree == M: # 딱! 맞으면 그거로 끝
            result = mid
            break

        elif current_get_tree < M: # 필요한 나무보다 적으면 절단기를 낮춰야 한다.
            right = mid - 1

        else: # 필요한 나무보다 더 많으면 절단기를 높여보자.(환경을 살리기 위해)
            left = mid + 1
            result = max(result, mid) # 일단 구해진 절단기 높이 저장


LowerBound(0, max_height)

print(result)


