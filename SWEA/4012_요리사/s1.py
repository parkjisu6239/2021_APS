import sys
from itertools import combinations
sys.stdin = open('input.txt')

def food(a, b):
    global min_cha
    a_score = 0
    b_score = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            a_score += synergy[a[i]][a[j]] + synergy[a[j]][a[i]]
            b_score += synergy[b[i]][b[j]] + synergy[b[j]][b[i]]
    cha = abs(a_score-b_score)
    if cha < min_cha:
        min_cha = cha


for tc in range(1, int(input())+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    min_cha = 99999999999
    ingredients = list(range(N))
    all_a = list(combinations(ingredients, N // 2))
    for a in all_a:
        b = []
        for ingredient in ingredients:
            if ingredient not in a:
                b.append(ingredient)

        food(a, b)

    print('#{} {}'.format(tc, min_cha))