import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    letters = input()
    stk = []
    for x in letters:
        if not stk:             # stk이 비었다면 문자 추가
            stk.append(x)
        else:
            if stk[-1] == x:    # 마지막 원소가 추가하려는 글자와 같은 경우 pop
                stk.pop()       # but stk[-1] 하기 전에도 if stk으로 검사해줘야함 !!!!
            else:
                stk.append(x)   # 같지 않은 경우는 stk에 추가

    print(f'#{test_case} {len(stk)}')

