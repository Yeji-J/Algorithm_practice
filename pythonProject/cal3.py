import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# 후위표기
def postF():
    stk = []
    for ch in st:
        if ch.isdigit():                        # push 숫자 into postFix
            postFix.append(ch)
        else:
            if ch == ')':                       # 닫힌 괄호

                while stk and stk[-1] != '(':   # 열린 괄호가 나올 때까지 pop
                    postFix.append(stk.pop())
                stk.pop()                       # 나온 열린괄호 pop

            elif ch == '*' or ch == '+':                        # 연산자

                while stk and out_stk[ch] <= in_stk[stk[-1]]:   # stk[-1] 우선순위가 낮아질 때까지
                    postFix.append(stk.pop())                   # pop & postFix에 push
                stk.append(ch)                              # 나온 연산자 push

            elif not stk or in_stk[stk[-1]] < out_stk[ch]:  # stk empty 혹은 stk[-1] 우선순위가 낮을 때
                stk.append(ch)                                  # stk에 push

    return stk

# 후위표기 계산
def cal():
    for x in postFix:
        if x.isdigit():         # 숫자 stk2에 push
            stk2.append(int(x))
        else:
            if len(stk2) >= 2:      # stk2에 피연산자 2개 이상
                op2 = stk2.pop()
                op1 = stk2.pop()
                if x == '+':                # 더하기 & stk2에 추가
                    stk2.append(op1 + op2)
                else:                       # 곱하기 & stk2에 추가
                    stk2.append(op1 * op2)
    return stk2

T = 10
for test_case in range(1, T+1):
    _ = input()
    st = input()

    out_stk = {')': 0, '+': 1, '*': 2, '(': 3}  # 스택 밖 우선순위
    in_stk = {')': 0, '+': 1, '*': 2, '(': 0}   # 스택 안 우선순위

    # 후위표기
    postFix = []
    postF()

    # 후위표기 계산
    stk2 = []
    cal()

    print(f'#{test_case}', *stk2)

