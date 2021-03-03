import sys
sys.stdin = open('input.txt')

print('Pascal')
print('size:1, row:0 | 1')
print('size:2, row:1 | 1 1')
print('size:3, row:2 | 1 2 1')
print('size:4, row:3 | 1 3 3 1')
print('size:5, row:4 | 1 4 6 4 1')
print('size:6, row:5 | 1 5 10 10 5 1')
print('size:7, row:6 | 1 6 15 20 15 6 1')
print('size:8, row:7 | 1 7 21 35 35 21 7 1')
print('size:9, row:8 | 1 8 28 56 70 56 28 8 1')
print('-----------------------------------')

def Pascal(size):
    pascal = [[1], [1, 1]] # 1,2번째는 모든 원소가 1
    # 사이즈가 1이면, 1만 출력
    if size == 1:
        print('1')
    # 사이즈가 2이면 1 / 1 1 만 출력
    elif size == 2:
        for p in pascal:
            print(' '.join(map(str, p)),end='\n')
    # 사이즈가 3 이상일 경우부터 계산하기
    else:
        # 위에서 1,2일때를 미리 계산해서, range(2, size)까지만
        for i in range(2, size): # i는 행
            # 맨 앞은 무조건 1
            temp = [1]
            # 중간에 오는 값을 계산
            for j in range(1, i): # j는 열
                val = pascal[i-1][j-1] + pascal[i-1][j]
                temp.append(val)
            # 맨 뒤도 무조건 1
            temp.append(1)
            # 지금까지 만든 것 pascal에 쌓기
            pascal.append(temp)
        # 출력하기
        for p in pascal:
            print(' '.join(map(str, p)),end='\n')

for tc in range(1, int(input())+1):
    size = int(input())
    print('#{}'.format(tc))
    Pascal(size) # 여러줄 출력이라 return 없는 함수로 생성