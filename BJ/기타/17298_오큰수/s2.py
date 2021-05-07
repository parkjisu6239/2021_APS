import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stack = [0]
result = [-1] * N
i = 1

# 정방향으로 가면서 스택에서 빠져나올때 result가 결정
# 점점 작아지는 동안에는 스택에 계속 추가, 도중에 큰 값이 나오면 while문을 순회하여
# 새로 나온 값보다 작았것들을 result갱신 해준다. 인덱스로 접근했기때문에 가능!
# 그러다 현재 스택에 있는게 더 커서 멈추면, 그 값도 스택에 추가하고 나머지 반복

while stack and i < N:
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)
