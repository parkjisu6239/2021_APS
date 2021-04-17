def solution(routes):
    routes.sort(key = lambda x : (x[1]))
    camera = routes[0][1]
    cnt = 1
    for i, o in routes:
        if i <= camera <= o:
            continue
        else:
            cnt += 1
            camera = o

    return cnt

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))