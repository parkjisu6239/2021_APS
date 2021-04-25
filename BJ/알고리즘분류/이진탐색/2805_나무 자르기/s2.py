import sys
sys.stdin = open('input.txt')

# input
N, M = map(int, input().split())
trees = list(map(int, input().split())) # 나무 최대 개수 100만

max_cuter = 1000000001
result = 0

def GetTree(cuter):
    get_tree = 0
    for tree in trees:
        if tree > cuter:
            get_tree += tree - cuter

    return get_tree


def FindMaxCutter(left, right):
    global result

    if left > right:
        return result

    mid = (left + right) // 2
    cut_tree = GetTree(mid)

    if cut_tree == M:
        result = mid
        return result
    elif cut_tree < M:
        return FindMaxCutter(left, mid - 1)
    else:
        result = max(result, mid)
        return FindMaxCutter(mid + 1, right)

FindMaxCutter(0, max_cuter)

print(result)


