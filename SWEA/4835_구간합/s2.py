import sys
sys.stdin = open("eval_input.txt", "r")

def Section_sum(N, M, numbers):
    # 편의상 큰 숫자를 N으로 지정
    if N < M:
        N, M = M, N

    # 첫번째 구간합을 구해, 최대최소 초기화
    section_sum = 0
    for i in range(M):
        section_sum += numbers[i]
    max_sum = min_sum =  section_sum

    # 위에서 구한거 다음부터 구할 것임
    for j in range(1, N-M+1):
        # 구간합의 경우 전구간과 현구간은 맨앞 맨뒤를 제외한 중간 부분은 중복됨
        # 그래서 현구간합은 앞에건 빼고, 뒤에건 더하면 됨
        section_sum = section_sum - numbers[j-1] + numbers[j+M-1]
        # 그렇게 구한 구간합이 min,max보다 크거나/작으면 최대최소로 지정
        if max_sum < section_sum:
            max_sum = section_sum
        if min_sum > section_sum:
            min_sum = section_sum

    return max_sum - min_sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, Section_sum(N, M, numbers)))