# 페르마의 소정리..?
# 자세한 설명 : https://st-lab.tistory.com/241

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

p = 1000000007
n, r = map(int, input().split())

fact = [1 for _ in range(n + 1)]


def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b//2) ** 2 * a) % p
    return (power(a, b//2) ** 2) % p


for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % p


A = fact[n]
B = (fact[n-r] * fact[r]) % p

print((A % p) * (power(B, p - 2) % p) % p)
