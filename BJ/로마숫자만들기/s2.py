N = 10

#N = int(input())

# 1 > 1,5,10,50 > 4
# 2 > 2,6,11,51 / (6),10,15,55 / (11),(15),20,60 / (51),(55),(60),100 > 중복되는게 나온 것은 제외
# 기본적으로 중복이 없다면 이전갯수*4 하지만 겹치는게 있음

numbers = [1, 5, 10, 50]
total = 0
visit = [0] * 1001
result = 0

def solution(idx, total, n):
    global result
    if idx == N:
        if not visit[total]:
            visit[total] = 1
            result += 1
        return

    # 매번 0~4로 두지 않는 이유?
    # 이전 재귀호출에서 반복되는 부분이 있을 것이기 때문!
    for i in range(n, 4):
        solution(idx+1, total + numbers[i], i)


solution(0, 0, 0)

print(result)