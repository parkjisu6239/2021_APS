def solution(arr1, arr2):
    # 진짜 그 행렬의 곱셈 arr1은 가로로 자르고 arr2세로로 잘라서 하는 그 진짜 곱셈
    answer = []
    # arr1은 행을 곱
    for arr1_row in arr1:
        answer_row = []
        # arr2는 열을 곱 zip으로 만들어줌
        for arr2_col in zip(*arr2):
            # 만들어준 행열을 zip으로 묶어서 각원소 a,b의 곱을 더함
            answer_row.append(sum(a*b for a, b in zip(arr1_row, arr2_col)))
        answer.append(answer_row)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))