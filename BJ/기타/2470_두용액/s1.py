import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

N = int(input())
potion = list(map(int, input().split()))
potion.sort()

s, e = 0, N-1
result = [ abs(potion[e] + potion[s]), s, e]

while s < e:
    if result[0] == 0:
        break

    mix = abs(potion[e] + potion[s]) # 새로 섞은게 최소이면
    if mix < result[0]: # 최소값 갱신
        result = [mix, s, e]

    # 앞,뒤 움직인 값
    s_move = abs(potion[s+1] + potion[e])
    e_move = abs(potion[s] + potion[e-1])

    if s + 1 == e: # 한개차이면 끝
        break

    if s_move < e_move:
        s += 1
    else:
        e -= 1

print(potion[result[1]], potion[result[2]])