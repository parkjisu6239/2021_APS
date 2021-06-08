import sys
sys.stdin = open("eval_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # N-1까지만 해도 정렬 완료!
    for i in range(N-1):
        # 최소값의 인덱스를 i라 하자
        min_idx = i
        # i+1부터 끝까지중에서 진짜 최소값인덱스를 찾자
        for j in range(i + 1, N):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        # 반복문이 종료되면, 찐최소값인덱스를 찾았다!
        # 그럼 최소값이랑, i랑 자리를 바꿔줘라!
        # 그럼 i가(정렬되지 않은 리스트에서 맨앞)가 최솟값이 되었다!!
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    print('#{}'.format(tc), end=" ")
    print(*numbers)
