import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    case = input()
    stk = []
    ans = 1
    for ch in case:
        if ch == '(' or ch == '{':         # 열린 괄호 push
            stk.append(ch)
        elif ch == ')':        # 닫힌 괄호 '(' 일 때
            if stk:
                if stk.pop() != '(':    # pop한 원소가 짝이 아니라면
                    ans = 0             # false
                    break
            else:
                ans = 0
                break
        elif ch == '}':
            if stk:
                if stk.pop() != '{':
                    ans = 0
                    break
            else:
                ans = 0
                break
    if stk:
        ans = 0

    print(f'#{test_case} {ans}')