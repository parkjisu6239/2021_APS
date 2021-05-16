import sys
sys.stdin = open('input.txt')

a, b = input().split()


if len(b) > len(a):
    a, b = b, a

bl = len(b)
al = len(a)

ans = ''
next = 0

for i in range(bl):
    hap = int(a[al-1-i]) + int(b[bl-1-i]) + next
    if hap > 9:
        next = 1
        hap -= 10
    else:
        next = 0

    ans = str(hap) + ans

if al == bl:
    if next:
        ans = str(next) + ans
else:
    for j in range(bl, al):
        hap = int(a[al - 1 - j]) +  next
        if hap > 9:
            next = 1
            hap -= 10
        else:
            next = 0

        ans = str(hap) + ans

print(ans)

