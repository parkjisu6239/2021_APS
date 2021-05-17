def solution(left, right):
    return sum([-num if int(num**0.5) == num**0.5 else +num for num in range(left, right+1)])


print(solution(13, 17))
print(solution(24, 27))


# def solution(left, right):
#     answer = 0
#
#     for num in range(left, right+1):
#         if int(num**0.5) == num**0.5:
#             answer -= num
#         else:
#             answer += num
#
#     return answer
