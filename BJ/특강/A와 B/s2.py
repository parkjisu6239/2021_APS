S = 'B'
T = 'ABBA'


S = input()
T = input()

que = [S]
flag = 0

while que:
    text = que.pop(0)
    if text == T:
        flag = 1
        break

    if len(text) < len(T):
        que.append(text+'A')
        que.append(text[::-1] + 'B')

print(flag)



