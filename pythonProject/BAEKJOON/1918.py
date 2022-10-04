import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

st = input()

out_stk = {'(': 0, '+': 1, '-': 1, '*':2, '/': 2, ')': 3}    # 스택밖 우선순위
in_stk = {'(': 0, '+': 1, '-': 1, '*':2, '/': 2, ')': 0}    # 스택안 우선순위

stk = []
res = []
for ch in st:
    if ch.isalpha():        # 알파벳이면 무조건 추가
        res.append(ch)

    else:                   # 알파벳이 아니면

        if ch == '(':       # 열린괄호일 때
            stk.append(ch)

        elif ch == ')':       # 괄호가 닫혔으면

            while stk and stk[-1] != '(':       # 열린 괄호 전까지 pop
                res.append(stk.pop())
            stk.pop()                           # 남아있는 열린괄호 pop

        elif ch == '*' or ch == '+' or ch == '-' or ch == '/':      # 연산자일 때

            # stk 마지막 값이 우선순위가 낮을 때까지 pop
            while stk and out_stk[ch] <= in_stk[stk[-1]]:
                res.append(stk.pop())
            stk.append(ch)          # 나온 연산자 stk에 push

        # stk empty 혹은 stk[-1] 우선순위가 낮을 때 stk에 push
        elif not stk or in_stk[stk[-1]] < out_stk[ch]:
            stk.append(ch)

# stk에 원소가 남아있으면
if stk:
    while stk:
        res.append(stk.pop())

print("".join(res))

