def solution(routes):
    highway = dict()
    for route in routes:
        for i in range(route[0], route[1] + 1):
            highway[i] = highway.get(i, 0) + 1


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))