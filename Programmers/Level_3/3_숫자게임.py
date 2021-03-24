# 1. 그냥 시간초과
# from itertools import permutations
# def solution(A, B):
#     max_score = 0
#     B_combi = list(permutations(B, len(B)))
#     for comB in B_combi:
#         score = 0
#         for i in range(len(A)):
#             if comB[i] > A[i]:
#                 score += 1
#         if score > max_score:
#             max_score = score
#     return max_score


#print(solution([5,1,3,7], [2,2,6,8]))


# 2. 효율성 시간초과
# def solution(A, B):
#     answer = 0
#     B.sort()
#     for i in range(len(B)):
#         for j in range(len(A)):
#             if A[j] < B[i]:
#                 answer += 1
#                 A[j] = 9000000000
#                 break
#
#     return answer


# 3. 통과!
def solution(A, B):
    # idea
    # A,B를 모두 정렬한 후 비교한다.
    # 만약 B 최소 카드가 A 최소카드보다도 작으면, B의 0번 사람은 그냥 누구랑 해도 진다.
    # 그렇다면, 다음 턴에서 확인 할 것은 A[0], B[1]이다. 즉, B가 진 경우에는 A 인덱스를 올리지 않는다.
    # 효율적으로 이기기 위해서는 값의 차이가 가장 적게 해서 이기는 것이기 때문이다.
    # 반대로, A[0], B[0] 비교시 B가 크다면, 다음턴에서는 둘다 인덱스를 올려서 A[1], B[1]을 비교한다.

    answer = 0
    A.sort()
    B.sort()
    j = 0
    for i in range(len(B)):
        while j < len(A):
            if A[j] < B[i]:
                answer += 1
                j += 1
                break
            else:
                break


    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))