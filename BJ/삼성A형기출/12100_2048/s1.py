import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move(blocks, direction):
    temp = []
    for r in range(N):
        stack1 = []
        for c in range(N):
            if direction in (0, 1):
                if blocks[r][c]:
                    stack1.append(blocks[r][c])
            else:
                if blocks[c][r]:
                    stack1.append(blocks[c][r])

        stack2 = []
        pre = 0 # 방금전에 합쳐졌는지 아닌지
        for s in stack1[::1 - 2*(direction%2)]:
            if stack2 and stack2[-1] == s and pre == 0:
                stack2[-1] *= 2
                pre = 1
            else:
                stack2.append(s)
                pre = 0

        blank = N - len(stack2)
        new_block = stack2 + [0] * blank
        if direction == 0:
            temp.append(new_block)
        else:
            temp.append(new_block[::-1])

    if direction in (0, 1):
        return temp
    else:
        return list(zip(*temp))


def findMax(block):
    MAX = 0
    for i in range(N):
        MAX = max(MAX, max(block[i]))

    return MAX

que = [(board, 0)]

result = 0

while que:
    block, cnt = que.pop(0)

    if cnt > 5: break

    result = max(result, findMax(block))

    for k in range(4):
        que.append((move(block, k), cnt + 1))

print(result)

