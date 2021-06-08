import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    A = input()
    B = input()

    if A * len(B) == B * len(A):
        print(1)
    else:
        print(0)

