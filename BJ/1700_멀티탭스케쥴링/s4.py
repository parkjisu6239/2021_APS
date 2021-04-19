import sys
import time
sys.stdin = open('input.txt')
start = time.time()

# 00. input
N, K = map(int, input().split())
items = list(map(int, input().split()))


# 01. 멀티탭에 꽂을수 있는 만큼 일단 꽂기
multitab = [0] * N
m = 0
i = 0
while  m < N: # 서로 다른 제품을 꽂기, 같은거 나오면 넘어가기
    if items[i] not in multitab:
        multitab[m] = items[i]
        m += 1
    i += 1


# 02. 멀티탭에 꽂은거 말고 남은 것들의 등장(향후 사용) 횟수 세기
C = [0] * (K+1)
for i in range(m, len(items)):
    C[items[i]] += 1


# 03. 멀티탭에서 뭘 뺄지 정하는 함수
def plug_out(t):
    for i in range(len(multitab)): # 멀티탭에 꽂힌 제품중에서
        if C[multitab[i]] == 0: # 더이상 안쓰는 제품이 있으면
            return i # 그걸 멀티탭에서 빼

    # 나중에 다 써야되는 제품인 경우
    # 제일 나중에 쓸걸 빼자
    out = 0
    for i in range(len(multitab)):
        item_use_idx = items[t+1:].index(multitab[i]) # 언제 또 쓰는지
        if item_use_idx >= out: # 더 늦게 쓰는것으로 갱신
            out = item_use_idx
            out_idx = i

    return out_idx # 제일 늦게 쓰는걸 빼기


# 04. 실행
result = 0
for t in range(m, len(items)): # 이미 꽂힌거 다음부터
    if items[t] not in multitab: # 새로 꽂아야 하는 경우
        off_idx = plug_out(t) # 뺄거 선택
        multitab[off_idx] = items[t] # 빼고 꽂고
        result += 1
    C[items[t]] -= 1 # 처리 완료했으니 등장횟수 -1


# 05. 출력
print(result)


print(time.time()-start)