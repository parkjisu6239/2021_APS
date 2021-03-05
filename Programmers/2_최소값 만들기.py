def solution(A, B):
    answer = []
    N = len(A)
    for i in range(N):
        for j in range(N):
            answer.append([i, j])

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))