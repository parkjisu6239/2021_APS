def solution(n, costs):
    def find(x): # 루트를 찾는 함수
        if x != parent[x]: # 내가 루트가 아니면
            parent[x] = find(parent[x]) # 부모노드로 올라가서 탐색을 다시
        return parent[x] # 루트 노드에 도달하면 루트를 리턴

    def union(a, b): # a, b 경로를 합치기 위함
        root_a = find(a) # 루트를 찾아서
        root_b = find(b)
        parent[root_b] = root_a # 루트를 연결

    costs.sort(key = lambda x : (x[2]))
    parent = [me for me in range(n)] # 정점의 부모노드를 저장

    result = 0 # 최소비용
    node = 0 # 연결한 간선 수

    for v, w, d in costs:
        if find(v) != find(w):
            union(v, w)
            result += d
            node += 1
        if node == n - 1:
            break

    return result

print(solution(4, [[0,1,1],[0,3,2],[1,2,3],[1,3,2],[2,3,4]]))