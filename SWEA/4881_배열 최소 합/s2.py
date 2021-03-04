import sys
sys.stdin = open('input.txt')

def ArrayMinSum(idx):
    global array_sum

    # 모든 행이 선택된 경우
    if idx == N:
        # 합을 구한다
        temp = 0
        for i in range(N):
            temp += number[i][visit[i]]
        if temp < array_sum:
            array_sum = temp
        return

    # 현재 idx 행에서 선택할 열 후보 0 ~ N-1
    for j in range(N):
        # 이미 선택된 열이라면, 더 이상 선택 불가!
        if check[j]: continue

        # 선택 가능한 열은 아래 코드로 내려 간다.
        # 현재 idx 행에서 j 열을 선택 완료!
        # 그렇다면 재귀적으로 다음 행도 열 선택 하러 ㄱㄱ
        check[j] = 1 # j열은 벌써 선택 되었으니, 선택 여부 1로 변경
        visit[idx] = j # 현재 idx 행에, j열을 선택했다는 의미로 방문 기록!
        ArrayMinSum(idx + 1) # 재귀적으로 다음 행으로 넘어간다
        check[j] = 0 # 함수 호출이 종료되고 아래로 내려왔을때, 선택했던 열을 선택 해제 해야한다.


for tc in range(1, int(input())+1):
    N = int(input())
    number = [ list(map(int, input().split())) for _ in range(N)]
    # N_queens과 유사하고, 대각선 고려를 안할 뿐!

    # 0행부터 체스판에 퀸을 놓듯이, 선택할 것.
    # 선택하려는 행 인덱스
    idx = 0

    # 열을 선택했는지 기록
    # ex) check[0] = 1 : 0열 선택이 완료되었다.
    # 그러니까 다음행부터는 0열에 놓을 수 없다.
    check = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]

    # 최종 결과물 최소값을 찾기 위해 갱신해줘야하므로 큰값을 지정
    array_sum = 99999999999999 # 실제 나올수 없는 큰~~~값

    # 첫행부터 시작
    ArrayMinSum(0)

    # 결과출력
    print('#{} {}'.format(tc, array_sum))
