import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cards = {}

for num in nums:
    cards[num] = cards.get(num, 0) + 1

M = int(input())

for key in map(int, input().split()):
    print(cards.get(key, 0), end=" ")
