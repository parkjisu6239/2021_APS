import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 1 : 1 ㅇ -> 1
# 2 : 11 -> 2
# 3 : 111 -> 3
# 4 : 121 ㅇ -> 3
# 5 : 1211 -> 4
# 6 : 1221 -> 4
# 7 : 11221 -> 5
# 8 : 12221 -> 5
# 9 : 12321 ㅇ -> 5


for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    result = 0

    i = 1
    while i*i <= distance:
        i += 1

    lte = (i-1)**2
    gte = i**2

    mid = (lte + gte -1)//2

    if lte == distance:
        result = 2*(i-1) - 1
    elif lte < distance <= mid:
        result = 2*i-1 -1
    elif mid < distance < gte:
        result = 2 * i - 1

    print(result)



