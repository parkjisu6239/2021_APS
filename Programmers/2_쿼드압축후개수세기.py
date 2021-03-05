def solution(arr):
    result = [0, 0]

    def Quard(arr):
        N = len(arr)
        # 원소가 한개 뿐이면, 그냥 0,1 개수 세기
        if N == 1:
            result[arr[0][0]] += 1
            return

        # 모든 원소가 같다면 나누지 않아도 됨
        temp = 0
        for i in range(N):
            for j in range(N):
                temp += arr[i][j]

        # 모든 원소 다 더한게 0이면, 모두 0
        if temp == 0:
            # 압축해서 1개로
            result[0] += 1
            # 더 쪼갤 필요 X
            return
        # 다 더한게 행렬크기와 같으면, 모두 1
        elif temp == N**2:
            # 압축하여 1개로
            result[1] += 1
            # 더 쪼갤 필요 X
            return

        # 모든 원소가 같지 않아서 4개로 쪼개야하는 경우
        # 일단 위아래 반반 쪼개
        top = arr[: N//2]
        bottom = arr[N//2 : ]
        q1, q2, q3, q4 = [], [], [], []

        for i in range(N//2):
            q1.append(top[i][:N//2])
            q2.append(top[i][N // 2:])
            q3.append(bottom[i][:N // 2])
            q4.append(bottom[i][N // 2:])

        Quard(q1)
        Quard(q2)
        Quard(q3)
        Quard(q4)


    Quard(arr)

    return result

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))