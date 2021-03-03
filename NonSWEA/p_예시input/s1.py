import sys

# sys.stdin = open("input.txt", "r")
sys.stdin = open("input.txt")

# 1. 홀짝구분
N = int(input())
print(N % 2)

# 2. 숫자합
numbers = list(map(int, input().split()))
hap = 0
for number in numbers:
    hap += number
print(hap)

# 3. 2행2열
M = int(input())
my_list = []
for _ in range(M):
    my_list.append(list(map(int, input().split())))
print(my_list[1][1])
