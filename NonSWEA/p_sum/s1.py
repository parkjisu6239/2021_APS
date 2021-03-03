import sys
sys.stdin = open("input.txt", "r")

def list_max_sum(number_list):

    # 행, 열, 대각선 최대값 초기화
    row_max = 0
    col_max = 0
    dia_max = 0

    # 대각선은 2개 중에 큰거 고르면 되고, 반복문안에서 초기화 할수 없기때문에 밖에서 초기화
    dia_sum1 = 0
    dia_sum2 = 0
    # 100 * 100 배열이라고 명시되어있기때문에 모든 행,열 100회씩 반복
    for i in range(100):
        # 첫번째 반복문 아래에서 합 초기화
        row_sum = 0
        col_sum = 0
        for j in range(100):
            # (행합은 ij, 열합은 ji) 위 반복문에서 고정한 i 인덱스를 행 or 열로 지정함
            row_sum += number_list[i][j]
            col_sum += number_list[j][i]
            # 오른쪽 아래로 가는 대각선의 합
            if i == j:
                dia_sum1 += number_list[i][j]
            # 왼쪽 아래로 가는 대각선의 합
            if i + j == 99:
                dia_sum2 += number_list[i][j]
        # j 반복문이 완료되면 1개의 행 or 열에 대한 행합 or 열합이 나오고, 그게 각각의 max보다 크면 max라고 지정
        if row_max < row_sum:
            row_max = row_sum
        if col_max < col_sum:
            col_max = col_sum

    # 대각선은 전체 반복문이 모두 수행된 이후에 구할 수있기때문에, 반복문이 완전히 종료된 이후에 최대값을 구함
    if dia_sum1 > dia_sum2:
        dia_max = dia_sum1
    else:
        dia_max = dia_sum2

    # 행최대, 열최대, 대각선최대 중에서 진짜 최대를 고름
    if row_max >= col_max and row_max >= dia_max:
        return row_max
    elif col_max >= row_max and col_max >= dia_max:
        return col_max
    else:
        return dia_max

for _ in range(10):
    N = int(input())
    number_list = [ list(map(int, input().split())) for _ in range(100) ]
    print('#{} {}'.format(N, list_max_sum(number_list)))