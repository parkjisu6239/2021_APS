import sys
sys.stdin = open("input.txt", "r")

def Extremeideugchung(month, price):
    global min_price, use_plan

    # 12달까지의 모든 조합이 끝나면 끝
    if month >= 12:
        if price < min_price:
            min_price = price
        return

    # (backtracking) 이미 최소값이 넘어갔다면 구하지 말자
    if price > min_price: return

    # 해당월을 1일 or 1개월 이용권중 싼것으로 이용하는 경우
    Extremeideugchung(month+1, price + min(use_plan[month]*prices[0], prices[1]))

    # 해당월을 3개월권으로 이용하는 경우
    Extremeideugchung(month+3, price + prices[2])


for tc in range(1, int(input())+1):
    # 특정달의 요금을 1일권, 한달권, 3달권으로 낼지 조합하여 최소의 값을 구해야한다.
    # 가격정보, 계획 인풋
    prices = list(map(int, input().split()))
    use_plan = list(map(int, input().split()))

    # 최소값
    min_price = 999999999999
    # 0월 부터 시작
    Extremeideugchung(0, 0)

    # 연간이용권과 비교
    if min_price < prices[3]:
        print('#{} {}'.format(tc, min_price))
    else:
        print('#{} {}'.format(tc, prices[3]))

