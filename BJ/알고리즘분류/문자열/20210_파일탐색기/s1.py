import sys

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
            if 48 <= ord(s) <= 57: # number
                num += s
            elif num:
                temp.append(num)
                num = ""
            else:
                temp.append(s)
        if num:
            temp.append(num)
        result.append(temp)
    return  result


def who_is_first(i, j):
    a = arr[i]
    b = arr[j]
    k = 0
    while True:
        if len(a) == k:
            return i

        if len(b) == k:
            return j

        if a[k] == b[k]:
            k += 1
            continue

        if 48 <= ord(a[k][0]) <= 57 and 48 <= ord(b[k][0]) <= 57: # both number
            if int(a[k]) < int(b[k]):
                return i
            else:
                return j
        elif ord(a[k][0]) >= 65 and ord(b[k][0]) >= 65: # both string
            if alpha[a[k]] < alpha[b[k]]:
                return i
            else:
                return j
        else: # mixed
            if ord(a[k][0]) < ord(b[k][0]):
                return i
            else:
                return j


def quick_sort(idx_arr):
    if len(idx_arr) < 2:
        return idx_arr

    left = []
    right = []
    pivot = idx_arr[0]

    for i in range(1, len(idx_arr)):
        if who_is_first(idx_arr[i], pivot) == idx_arr[i]:
            left.append(idx_arr[i])
        else:
            right.append(idx_arr[i])

    return [*quick_sort(left), pivot, *quick_sort(right)]



arr = processed_arr(_arr)
sorted_idx = quick_sort([idx for idx in range(n)])

for idx in sorted_idx:
    print(_arr[idx])