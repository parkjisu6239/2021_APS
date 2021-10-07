# 1 2
# 2 2

# 1 2 3 4 5 6
# 2 2 3 4 5 6
# 3 3 3 4 5 6
# 4 4 4 4 5 6
# 5 5 5 5 5 6
# 6 6 6 6 6 6

# 1 2 3 4 5 6 / 2 2 3 4 5 6 / 3 3 3 4 5 6 / 4 4 4 4 5 6 / 5 5 5 5 5 6 / 6 6 6 6 6 6

# 위 1차원 행렬을 n개씩 끊었을때 i번째는 i가 i번 나오는것부터 시작함
# 시작점은 left를 n으로 나눴을 때 몫

def solution(n, left, right):
    answer = []
    start_num, remainder = divmod(left, n)
    lenght = (right - left)//n + 1
    for i in range(start_num+1, start_num + lenght+2):
        temp = [i] * i
        for j in range(i+1, n+1):
            temp.append(j)
        answer.extend(temp)

    return answer[remainder: remainder + right - left+1]

print(solution(3, 2, 5))
print(solution(4, 7, 14))
