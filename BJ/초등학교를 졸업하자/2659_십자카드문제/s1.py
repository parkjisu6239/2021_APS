import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

cards = list(map(int, input().split()))
candis = []


def get_clock_number():
    for i in range(4):
        temp = 0
        for j in range(4):
            temp += cards[(i+j)%4]*(10**(3-j))
        candis.append(temp)

    return min(candis)


def get_ans(limit):
    cnt = 0
    for num in range(1111, limit + 1):
        if is_clock_number(num):
            cnt += 1
    return cnt


def is_clock_number(num):
    candi = []
    st_num = str(num)

    for i in range(4):
        temp = ""
        for j in range(4):
            temp += st_num[(i+j)%4]
        candi.append(temp)

    if int(min(candi)) == num:
        return True

    return False


target = get_clock_number()
print(get_ans(target))

