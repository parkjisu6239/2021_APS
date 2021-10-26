import sys
sys.stdin = open('input.txt')

letter = input()
stack = []
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
after = ""

for l in letter:
    if l in ('*', '/', '+', '-'):
        while stack and priority[stack[-1]] >= priority[l]:
            if stack[-1] != '(':
                after += stack.pop()
            else:
                stack.pop()
                break
        stack.append(l)
    elif l == '(':
        stack.append(l)
    elif l == ')':
        while stack[-1] != '(':
            after += stack.pop()
        stack.pop()
    else:
        after += l

for i in range(len(stack)-1, -1, -1):
    after += stack[i]

print(after)