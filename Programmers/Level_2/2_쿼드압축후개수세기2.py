def solution(arr):
    result = [0, 0]

    def Quard(arr):
        N = len(arr)
        # 원소가 한개 뿐이면, 그냥 0,1 개수 세기
        if N == 1:
            result[arr[0][0]] += 1
            return

        # 모든 원소가 같은지 확인, 같다면 압축
        flag = 1
        a = arr[0][0]
        for i in range(N):
            if flag:
                for j in range(N):
                    if arr[i][j] != a:
                        flag = 0
                        break
            else:
                break

        if flag:
            result[a] += 1
            return

        # 모든 원소가 같지 않아서 4개로 쪼개야하는 경우
        # 일단 위아래(행으로) 반반 쪼개
        top = arr[: N // 2]
        bottom = arr[N // 2:]
        q1, q2, q3, q4 = [], [], [], []

        # 앞뒤(열로) 반반 쪼개
        for i in range(N // 2):
            q1.append(top[i][:N // 2])
            q2.append(top[i][N // 2:])
            q3.append(bottom[i][:N // 2])
            q4.append(bottom[i][N // 2:])

        # 4등분한거 각자 재귀 ㄱ
        Quard(q1)
        Quard(q2)
        Quard(q3)
        Quard(q4)

    Quard(arr)

    return result

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))