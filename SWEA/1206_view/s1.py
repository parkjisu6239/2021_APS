import sys
sys.stdin = open("eval_input.txt", "r")

def chek_View(buildings):
    # 조망권이 확보된 건물의 수
    result = 0
    # 앞뒤 2칸은 보지 않을 것임
    for i in range(2, T-2):
        # 이웃은 나를 포함한 앞뒤 2개의 건물(나까지 총 5개)
        neighborhood = buildings[i - 2:i + 3]
        # 이웃중에서 내가 제일 커야 조망권이 확보됨!
        if buildings[i] == max(neighborhood):
            # 그리고 나를 제외한 이웃중에서 가장 높은 건물의 높이
            neighborhood.remove(buildings[i])
            # 그 높이와 내 건물의 높이 차이가 조망권을 확보한 층 수!
            result += buildings[i] - max(neighborhood)
    return result
    
for i in range(1, 11):
    T = int(input())
    buildings = list(map(int, input().split()))
    ans = chek_View(buildings)
    print('#{} {}'.format(i, ans))

'''
def chek_View(buildings):
    # 조망권이 확보된 건물의 수
    result = 0
    # 앞뒤 2칸은 보지 않을 것임
    for i in range(2, T-2):
        # 이웃 건물은 내 기준 양옆 2개
        neighborhoods = buildings[i - 2:i] + buildings[i + 1:i + 3]
        # 이웃 건물 중 가장 높은 건물의 높이
        max_neighborhood = 0

        # 이웃 건물중 가장 높은 건물 찾기
        for neighborhood in neighborhoods:
            if neighborhood >= max_neighborhood:
                max_neighborhood = neighborhood

        # 내건물이랑 이웃중 최고건물 높이 차이
        building_height = buildings[i] - max_neighborhood
        
        # 내가 이웃중에 가장 높지 않으면, 내건물-이웃중최고가 음수가 나옴
        # 그러면 조망권 확보 안되는 거임
        # 그래서 양수일때만 더함
        if building_height > 0:
            result += building_height

    return result

for i in range(1, 11):
    T = int(input())
    buildings = list(map(int, input().split()))
    ans = chek_View(buildings)
    print('#{} {}'.format(i, ans))
'''