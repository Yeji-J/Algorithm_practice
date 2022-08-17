import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    st = input()
    stk = []
    ans = 1
    for ch in st:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:         # if stack has data in it
                stk.pop()
            else:           # if stack is empty
                ans = 0
                break

    if stk:                 # process finished, stack not empty
        ans = 0

    print(f'#{test_case} {ans}')

