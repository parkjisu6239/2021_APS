def solution(key, lock):
    # 0, 90, 180, 270 회전한 4개의 키의 1의 좌표값들
    # 자물쇠 기준으로 위에서부터 0의 좌표값들

    # 1. 자물쇠 순회하여 0인 좌표 찾기
    L = len(lock)
    locker = []
    for i in range(L):
        for j in range(L):
            if lock[i][j] == 0:
                locker.append((i, j))

    # 1-1. 자물쇠가 벌써 다 1이면 이미 열려있는거라서 True
    if not locker:
        return True


    # 2. key 순회하여 1인 좌표 찾기
    K = len(key)
    keys = [[], [], [], []]
    for i in range(K):
        for j in range(K):
            if key[i][j]:
                keys[0].append((i, j))

    # 2-1. key에 1인 부분이 없으면 열수 없음 False
    if not keys[0]:
        return False


    # 3. temp 회전하여 얻은 것들 key에 추가
    for i in range(3):
        for x, y in keys[i]:
            keys[i + 1].append((y, K - 1 - x))


    # 4. locks와 keys 맞춰보기
    # key중에 어느 하나가 locker의 맨위 구멍과 맞다고 할때,
    # 그 둘의 이동 거리를 구해서 나머지 key들을 이동시켜 본다. (평행이동)
    # 그러면 이때 열쇠와 키가 맞고, 안맞는것들은 인덱스 벗어난거면 True
    # 키가 안맞는데, 인덱스 안벗어났으면 충돌하는 부분이 있는거니 False
    for key in keys: # 4방 회전 확인
        for kr, kc in key: # 기준 키
            # 기준키(key의 한개 원소)가 locker[0]에 맞다고 하고, 그때 평행이동 거리 저장
            dr, dc = locker[0][0] - kr, locker[0][1] - kc
            matchs = [(kr, kc)] # 맞은 것들 저장
            for kr2, kc2 in key:
                if (kr, kc) != (kr2, kc2): # 기준키가 아니고
                    trans_r, trans_c = kr2 + dr, kc2 + dc # 평행 이동한 값
                    if (trans_r, trans_c) in locker: # 자물쇠와 맞는 경우
                        matchs.append((trans_r, trans_c))
                    elif trans_r < 0 or trans_c < 0 or trans_r >= L or trans_c >= L: # 인덱스 넘쳐서 나간경우
                        continue
                    else: # 맞지도 않는데, 인덱스 안넘치면 돌기부분끼리 만난 것
                        break
            else: # break 안걸리고
                if len(matchs) == len(locker): # 실제로 맞물린 부분과 자물쇠 0부분 갯수가 같으면 true
                    return True

    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))