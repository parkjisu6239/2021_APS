import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = int(input())

for i in range(a):
    b = int(input())
    temp = []
    for j in range(b):
        temp.append(list(map(int, sys.stdin.readline().split(" "))))

    # print(temp)

    temp = sorted(temp, key=lambda x: x[1], reverse=False)

    print(temp)

    ct = 1
    max_score = temp[0][0]
    for k in range(1, len(temp)):
        if temp[k][0] < max_score:
            ct += 1
            max_score = temp[k][0]
    print(ct)