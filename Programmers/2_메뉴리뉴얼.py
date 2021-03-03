def solution(orders, course):
    answer = []
    course_menu = dict()
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):
            menu = ''.join(sorted(map(str, set(orders[i]) & set(orders[j]))))
            if len(menu) >= 2:
                for k in range(1 << len(menu)):
                    temp = ''
                    for l in range(len(menu)):
                        if k & (1 << l):
                            temp += menu[l]
                    if len(temp) >= 2:
                        course_menu[temp] = course_menu.get(temp, 0) + 1
            elif len(menu) > 1:
                course_menu[menu] = course_menu.get(menu, 0) + 1
    print(course_menu)
    return sorted(course_menu)

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# 문제발견! 교집합으로 했더니 abcd 와 abcf의 교집합은 abc로 한개만 나온다
# 근데 문제에서는 중복코스 모두를 찾아야해서 ab bc ac abc이렇게 4개의 중복조합이 있다
