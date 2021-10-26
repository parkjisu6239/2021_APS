#96

import sys
sys.stdin = open('input.txt')

s = input()
ans = set()


def remove_bracket(idx, new_s, stack):
    if idx == len(s):
        if not stack: # 짝이 다 맞는 경우
            ans.add(new_s)
        return

    if s[idx] == "(":
        remove_bracket(idx + 1, new_s + s[idx], stack + [1]) # 괄호 제거 X
        remove_bracket(idx + 1, new_s, stack + [0]) # 괄호 제거
    elif s[idx] == ")" and stack:
        if stack[-1] == 0: # 짝꿍 괄호를 지웠던 경우
            stack.pop()
            remove_bracket(idx + 1, new_s, stack)  # 괄호 제거
        else: # 짝꿍 괄호를 지우지 않았던 경우
            stack.pop()
            remove_bracket(idx + 1, new_s + s[idx], stack)  # 괄호 제거 X
    else:
        remove_bracket(idx + 1, new_s + s[idx], stack)  # 괄호 제거 X


remove_bracket(0, "", [])

for answer in sorted(list(ans - {s})):
    print(answer)



