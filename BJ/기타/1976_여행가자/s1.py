import sys
sys.stdin = open('eval_input.txt')

# 그룹나누기 같은 문제라 서로소 집합 이용.
def find_set(x):
    if x != p[x]:
        return find_set(p[x])
    return x

def union(x, y):
    p[(find_set(y))] = find_set((x))


# input
V = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(V)] # 정점 연결 정보
plan = list(map(int, input().split()))

# 크루스칼을 위해 간선 연결 정보로 바꾸기
node = []
for i in range(V):
    for j in range(V):
        if graph[i][j]:
            node.append((i, j))

# 부모정보 초기화
p = list(range(V))

# 루트가 다르면 합치기
for x, y in node:
    if find_set(x) != find_set(y):
        union(x, y)

# 여행 계획 중에서, 서로 다른 루트를 담기
result = set()
for i in plan:
    result.add(find_set(i-1))

# 루트가 다른건 서로소집합이라, 루트가 한개인 경우만 가능
print('YES') if len(result) == 1 else print('NO')



