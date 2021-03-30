N = 2
#N = int(input())

result = []

def solution(num, cnt):
    if cnt == N:
        if num not in result:
            result.append(num)
        return

    solution(num + 1, cnt + 1)
    solution(num + 5, cnt + 1)
    solution(num + 10, cnt + 1)
    solution(num + 50, cnt + 1)

solution(0, 0)

print(len(result))