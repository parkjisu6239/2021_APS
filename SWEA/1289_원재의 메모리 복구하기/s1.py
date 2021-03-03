import sys
sys.stdin = open("input.txt")

def Memory(memory):
    bit_zero = [0] * len(memory) # 초기값 0000~000
    result = 0 # 고친 횟수
    while bit_zero != memory: # 다를때만 반복
        for i in range(len(memory)): # 처음으로 다른 지점을 찾자
            if memory[i] != bit_zero[i]: # 그 지점 이후로 모두 0 또는 1로 변경
                for j in range(i,len(bit_zero)):
                    bit_zero[j] = memory[i]
                result += 1 # 한번 고쳤으니, 고친횟수 +1
                break

    return result

for tc in range(1, int(input()) + 1):
    print('#{} {}'.format(tc, Memory(list(map(int, input())))))