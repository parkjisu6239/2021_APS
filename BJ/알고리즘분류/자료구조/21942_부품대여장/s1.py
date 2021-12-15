import sys
sys.stdin = open('input.txt')
read = sys.stdin.readline

N, L, F = map(str, read().split())
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
limit = int(L[:3])*24*60 + int(L[4:6])*60 + int(L[7:])
fee = int(F)
rental = {}
overdue = {}

for _ in range(int(N)):
    date, time, item, name = map(str, read().split())
    rental[name] = rental.get(name, {})
    year, month, day = map(int, date.split('-'))
    h, m = map(int, time.split(':'))
    time_id = (sum(month_days[:month]) + day - 1) * 24 * 60 + h * 60 + m

    if rental[name].get(item, 0) == 0: # 빌리는 경우
        rental[name][item] = time_id
    else: # 반납하는 경우
        if time_id - rental[name][item] > limit: # 연체
            overdue_fee = (time_id - rental[name][item] - limit) * fee
            overdue[name] = overdue.get(name, 0) + overdue_fee
        del rental[name][item]

names = sorted(list(overdue))
if names:
    for name in names:
        print(name, overdue[name])
else:
    print(-1)