import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = 3
for test_case in range(1, T+1):
    _, pw = input().split()
    stk = []
    for x in pw:            # pw 각 숫자(str type)에 대해
        if stk:             # stk not empty
            if stk[-1] == x:    # 마지막 원소와 같다면
                stk.pop()       # 제거
            else:
                stk.append(x)   # 다르다면 추가
        else:
            stk.append(x)       # stk empty => 추가

    stk = ''.join(stk)

    print(f'#{test_case} {stk}')
