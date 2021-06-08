import sys
sys.stdin = open('eval_input.txt')

def n_to_decimal(num, n):
    result = 0
    for i in range(len(num)):
        result += int(num[i])*(n**(len(num)-i-1))
    return result

def change_one(num, k):
    changes = set()
    for j in range(len(num)):
        for l in range(k):
            if num[j] != str(l):
                change_num = num[:j] + str(l) + num[j + 1:]
                changes.add(n_to_decimal(change_num, k))

    return changes


for tc in range(1, int(input())+1):
    two = change_one(input(), 2)
    three = change_one(input(), 3)
    print('#{} {}'.format(tc, *two&three))