import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    st = input().split()
    stk = []
    ans = 0
    for ch in st:
        if ch.isdigit():                    # 숫자일 때
            stk.append(int(ch))
        elif ch == '.':                     # '.'일 때 pop 후 종료
             ans = stk.pop()
             break
        else:                       # 연산자일 때
            if len(stk) >= 2:           # 피연산자 두 개 이상
                op2 = stk.pop()         # 처음 꺼낸 숫자 op2로
                op1 = stk.pop()
                if ch == '+':
                    stk.append(op1 + op2)
                elif ch == '*':
                    stk.append(op1 * op2)
                elif ch == '/':
                    stk.append(op1 // op2)      # 안 나누어 떨어져도 강제로 떨어지게^^!!
                else:
                    stk.append(op1 - op2)
            else:
                ans = 'error'           # 피연산자 1개 이하
                break

    if len(stk) >= 2:                   # 연산 종료 but 스택 내 숫자 2개 이상
       ans = 'error'

    print(f'#{test_case} {ans}')

