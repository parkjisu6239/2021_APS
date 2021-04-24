def solution(nodeinfo):
    nodes = [] # 인덱스도 필요해서 새로 리스트 생성
    depth_temp = set() # y좌표의 수를 알기 위해
    max_x = 0 # x 최대범위 알기 위해

    for i in range(len(nodeinfo)):
        nodes.append([i + 1, nodeinfo[i][0], nodeinfo[i][1]])
        max_x = max(max_x, nodeinfo[i][0])
        depth_temp.add(nodeinfo[i][1])

    depth = len(depth_temp) # 트리의 뎁스

    # 인덱스, x, y, 자식의 x 최소, 자식의 x 최대
    # 완전이진트리로 표현하되 없으면 0,0,0,0,0
    tree = [[0, 0, 0, 0, 0] for _ in range(2**(depth+1))] # 꽉찬완전이진트리인경우까지

    # y 내림차순,x 오름차순하면 그림처럼
    nodes.sort(key=lambda x: (-x[2], x[1]))

    # 부모는 항상 맨앞에 것
    tree[1] = nodes[0]+[0, max_x]
    tree_idx = 1
    high = nodes[0][2] # 높이
    level = 0
    for nodes_idx in range(1, len(nodes)):
        if nodes[nodes_idx][2] != high: # 높이가 달라지면, 뎁스가 깊어진 것
            high = nodes[nodes_idx][2] # 높이 갱신
            level += 1 # 뎁스 갱신
            tree_idx = 2**level # 인덱스 갱신

        while True:
            if tree[tree_idx//2][1] and nodes[nodes_idx][1] < tree[tree_idx//2][1]: # 부모x값보다 작으면 왼
                if tree[tree_idx//2][3] <= nodes[nodes_idx][1] <= tree[tree_idx//2][4]: # 자식 범위에도 들어가면
                    tree[tree_idx] = nodes[nodes_idx] + [tree[tree_idx//2][3], tree[tree_idx//2][1]] # 저장
                    break
            if tree[tree_idx//2][1] and nodes[nodes_idx][1] > tree[tree_idx//2][1]: # 부모x값보다 크면 오른
                if tree[tree_idx//2][3] <= nodes[nodes_idx][1] <= tree[tree_idx//2][4]: # 자식 범위에도 들어가고
                    tree[tree_idx+1] = nodes[nodes_idx] + [tree[tree_idx // 2][1], tree[tree_idx // 2][4]]
                    tree_idx += 2
                    break
            tree_idx += 2


    ## 순회 ##
    pre = []
    post = []

    def pre_order(node):
        if tree[node][0]: # 유효하면
            pre.append(tree[node][0])
            pre_order(node * 2)
            pre_order(node * 2+1)

    def post_order(node):
        if tree[node][0]: # 유효하면
            post_order(node * 2)
            post_order(node * 2+1)
            post.append(tree[node][0])

    pre_order(1)
    post_order(1)

    return [pre, post]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
