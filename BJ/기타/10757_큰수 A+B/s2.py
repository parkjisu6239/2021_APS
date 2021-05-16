import sys
sys.stdin = open('input.txt')

a, b = input().split()

al = len(a)
bl = len(b)

if bl > al:
    a = '0'*(bl-al) + a
elif al > bl:
    b = '0' * (al - bl) + b

L = len(a)

ans = ''
next = 0

for i in range(L-1, -1, -1):
    hap = int(a[i]) + int(b[i]) + next
    if hap > 9:
        next = 1
        hap -= 10
    else:
        next = 0

    ans = str(hap) + ans

if next:
    ans = str(next) + ans

print(ans)
print(int(a) + int(b))

