import sys
sys.stdin = open('input.txt')

temp = int(input())
N = 0

while temp > 1:
    temp //= 3
    N += 1

pattern = ['***', '* *', '***']

pattern_re = [''] * 9




