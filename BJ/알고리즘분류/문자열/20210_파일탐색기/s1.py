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
            if s.isdigit():  # number
                num += s
                continue
            elif num:
                temp.append(num)
                num = ""
            temp.append(s)
        if num:
            temp.append(num)
        result.append(temp)
    return result


def who_is_first(i, j):
    a = arr[i]
    b = arr[j]
    k = 0
    while True:
        if len(a) == k:
            return i

        if len(b) == k:
            return j

        if a[k].isdigit() and b[k].isdigit(): # both number
            if int(a[k]) == int(b[k]):
                if len(a[k]) == len(b[k]):
                    k += 1
                    continue
                if len(a[k]) < len(b[k]):
                    return i
                elif len(a[k]) > len(b[k]):
                    return j
            elif int(a[k]) < int(b[k]):
                return i
            else:
                return j
        elif a[k].isalpha() and b[k].isalpha(): # both string
            if a[k] == b[k]:
                k += 1
                continue
            if alpha[a[k]] < alpha[b[k]]:
                return i
            elif alpha[a[k]] > alpha[b[k]]:
                return j
        else: # mixed
            if a[k].isdigit():
                return i
            else:
                return j

        k += 1
        continue


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
