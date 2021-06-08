import sys
sys.stdin = open('eval_input.txt')

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
result = 0
node = 0

for s, e, w in edges:
    if find_set(s) != find_set(e):
        union(s, e)
        result += w
        node += 1
    if node == V-1:
        break

print(result)





