import sys
sys.stdin = open('eval_input.txt')

def find_set(x): # 루트를 찾는 동시에, p에 항상 루트를 담음
    if x != p[x]:
        p[x] = find_set(p[x])
        return p[x]
    else:
        return x

def union(x, y): # 합치기
    x = find_set(x)
    y = find_set(y)
    if x != y:
        p[y] = x


V, E = map(int, input().split())
p = list(range(V+1))

for _ in range(E):
    uni_inter, a, b = map(int, input().split())
    if uni_inter: # 교집합 : 교집합인가?
        print('YES') if find_set(a) == find_set(b) else print('NO')
    else: # 합집합 : 합쳐라
        union(a, b)




