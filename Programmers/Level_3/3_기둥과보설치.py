def solution(n, build_frame):
    answer = [[]]
    arr = [[0] * n for _ in range(n)]

    # 기둥을 세우려면 기둥 왼쪽에 보가 있거나, 아래에 보가 있어야 함
    # 보를 세우려면 보 아래에 기둥이 있거나, 오른쪽 아래에 기둥이 있거나, 양쪽에 보

    return 0

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))