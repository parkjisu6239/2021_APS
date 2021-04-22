import sys
sys.stdin = open('input.txt')


# 프림은 메모리 초과..#

# 크루스칼 #
def find_set(x): # 루트를 찾는 동시에, p에 항상 루트를 담음
    if x != p[x]:
        p[x] = find_set(p[x])
        return p[x]
    else:
        return x

def union(x, y): # 합치기
    p[find_set(y)] = find_set(x)


V, E = map(int, input().split())
p = list(range(V+1))
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda x : (x[2]))
result = []
node = 0

for s, e, w in edges:
    if find_set(s) != find_set(e):
        union(s, e)
        result.append(w)
        node += 1
    if node == V-1:
        break

# 일단 최소신장트리를 찾으면 마을이 길 1개로 다 연결된다
# 이때 제일 긴거 한개 빼면 두개로 나뉘어진다.
print(sum(result)-max(result))





